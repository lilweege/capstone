from transformers import RobertaTokenizer, RobertaModel, AutoTokenizer, AutoModel
import torch
import os
import ast
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from tqdm import tqdm
from sklearn.metrics.pairwise import cosine_similarity
import json
import math
import re
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
import hashlib


# Device Configuration
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")


# ===========================
#  Token-Based Similarity
# ===========================
class TokenSimilarity:
    def __init__(self):
        self.vectorizer = CountVectorizer()

    def preprocess(self, code):
        """Preprocess code to normalize and replace variables for better token-based similarity."""
        # Remove comments and docstrings
        code = re.sub(r'(""".*?"""|\'\'\'.*?\'\'\'|#.*?$)', '', code, flags=re.MULTILINE | re.DOTALL)
        
        # Normalize whitespace
        code = re.sub(r'\s+', ' ', code).strip()

        # Replace variable names and function names
        tokens = re.findall(r'\b[a-zA-Z_]\w*\b', code)  # Extract tokens that look like variable names
        counts = Counter(tokens)

        # Replace variables that appear frequently (likely not keywords)
        replacements = {var: f"var_{i}" for i, (var, _) in enumerate(counts.items()) if not self.is_keyword(var)}
        
        for var, replacement in replacements.items():
            code = re.sub(rf'\b{var}\b', replacement, code)
        
        return code

    def is_keyword(self, token):
        """Check if a token is a Python keyword."""
        import keyword
        return token in keyword.kwlist

    def compute(self, code1, code2):
        """Compute token-based similarity after preprocessing."""
        # Preprocess both code snippets
        code1 = self.preprocess(code1)
        code2 = self.preprocess(code2)

        # Tokenize and vectorize the code
        vectors = self.vectorizer.fit_transform([code1, code2]).toarray()

        # Convert to tensors and normalize
        tensor1 = torch.tensor(vectors[0], dtype=torch.float32)
        tensor2 = torch.tensor(vectors[1], dtype=torch.float32)

        # Handle edge case where tensors have zero magnitude
        if torch.norm(tensor1) == 0 or torch.norm(tensor2) == 0:
            return 0.0  # If either vector is all zeros, similarity is 0.0

        # Compute cosine similarity
        cosine_sim = (tensor1 @ tensor2) / (torch.norm(tensor1) * torch.norm(tensor2))

        # Handle NaN (from division by zero) and clamp similarity to [0, 1]
        if torch.isnan(cosine_sim):
            return 0.0
        
        # Clamp to avoid floating point issues exceeding 1.0
        cosine_sim = torch.clamp(cosine_sim, 0.0, 1.0)
        
        # Apply tolerance check to treat near-1.0 values as exactly 1.0
        if torch.isclose(cosine_sim, torch.tensor(1.0), atol=1e-6):
            return 1.0

        return cosine_sim.item()


# ===========================
#  AST-Based Similarity
# ===========================
class ASTSimilarity:
    def __init__(self):
        # Dictionary for AST node types
        self.nodetypedict = {node: i for i, node in enumerate(ast.__dict__.keys())}

    def create_adjacency_matrix(self, ast_tree):
        """Generate an adjacency matrix from an AST tree."""
        matrix_size = len(self.nodetypedict)
        matrix = np.zeros((matrix_size, matrix_size))

        def traverse(node, parent=None):
            """Recursive traversal of the AST tree."""
            if not isinstance(node, ast.AST):
                return
            
            current_type = self.nodetypedict.get(type(node).__name__, -1)
            parent_type = self.nodetypedict.get(type(parent).__name__, -1) if parent else -1

            if parent is not None and current_type >= 0 and parent_type >= 0:
                matrix[parent_type][current_type] += 1

            for child in ast.iter_child_nodes(node):
                traverse(child, parent=node)

        traverse(ast_tree)

        # Normalize the matrix row-wise (only if total is greater than zero)
        for row in range(matrix.shape[0]):
            total = matrix[row].sum()
            if total > 0:
                matrix[row] /= total
        
        return matrix

    def compute_similarity(self, matrix1, matrix2):
        """Compute cosine similarity between two matrices."""
        vec1 = matrix1.flatten().reshape(1, -1)
        vec2 = matrix2.flatten().reshape(1, -1)
        similarity = cosine_similarity(vec1, vec2)[0][0]
        return similarity

    def compute(self, code1, code2):
        """Compute AST similarity between two code snippets."""
        tree1 = ast.parse(code1)
        tree2 = ast.parse(code2)
        matrix1 = self.create_adjacency_matrix(tree1)
        matrix2 = self.create_adjacency_matrix(tree2)
        return float(self.compute_similarity(matrix1, matrix2))


# ===========================
#  Model-Based Similarity (RoBERTa or CodeBERT)
# ===========================
class EmbeddingSimilarity:
    def __init__(self, model_name="FacebookAI/roberta-base", batch_size=8):
      if "roberta" in model_name.lower():
          self.tokenizer = RobertaTokenizer.from_pretrained(model_name)
          self.model = RobertaModel.from_pretrained(model_name)
      else:
          self.tokenizer = AutoTokenizer.from_pretrained(model_name)
          self.model = AutoModel.from_pretrained(model_name).to(device)
      
      # Cache to store embeddings
      self.embedding_cache = {}
      self.batch_size = batch_size

    def hash_code(self, code):
        """Generate a hash for the code snippet."""
        return hashlib.sha256(code.encode('utf-8')).hexdigest()

    def get_embedding(self, code_snippets):
        """Batch embedding generation with caching."""
        # Prepare for batch processing
        to_process = []
        to_process_indices = []
        embeddings = []

        # Check for cached embeddings first
        for idx, code in enumerate(code_snippets):
            code_hash = self.hash_code(code)
            if code_hash in self.embedding_cache:
                embeddings.append(self.embedding_cache[code_hash])
            else:
                to_process.append(code)
                to_process_indices.append(idx)

        # If all are cached, return early
        if not to_process:
            return torch.stack(embeddings)

        # Tokenize in batches
        for i in range(0, len(to_process), self.batch_size):
            batch = to_process[i : i + self.batch_size]
            inputs = self.tokenizer(
                batch,
                return_tensors="pt",
                max_length=512,
                truncation=True,
                padding="max_length"
            )
            inputs = {key: val.to(device) for key, val in inputs.items()}

            with torch.no_grad():
                outputs = self.model(**inputs)
                batch_embeddings = outputs.last_hidden_state[:, 0, :]

            # Cache and gather embeddings
            for j, embedding in enumerate(batch_embeddings):
                code_hash = self.hash_code(batch[j])
                self.embedding_cache[code_hash] = embedding
                embeddings.append(embedding)

        return torch.stack(embeddings)
  
    def compute(self, code1, code2):
      """Compute cosine similarity between embeddings of two code snippets."""
      embeddings = self.get_embedding([code1, code2])
      embedding1, embedding2 = embeddings[0], embeddings[1]

      cosine_sim = torch.nn.functional.cosine_similarity(
          embedding1.unsqueeze(0), embedding2.unsqueeze(0)
      ).item()

      # Normalize cosine similarity
      normalized_embed_sim = max(0.0, min(1.0, (cosine_sim - 0.99) * 100))
      return 1 / (1 + math.exp(-9 * (normalized_embed_sim - 0.5)))


# ===========================
#  Code Similarity Pipeline
# ===========================
class CodeSimilarityPipeline:
    def __init__(self, model_name="FacebookAI/roberta-base"):
        self.token_sim = TokenSimilarity()
        self.ast_sim = ASTSimilarity()
        self.embed_sim = EmbeddingSimilarity(model_name)
    
    def read_code_files_for_question(directory, question_folder):
      """Read Python files from a specific question folder."""
      file_pairs = []
      question_path = os.path.join(directory, question_folder)
      if os.path.isdir(question_path):
          python_files = [f for f in os.listdir(question_path) if f.endswith('.py') and is_python3_file(os.path.join(question_path, f))]
          for i, file1 in enumerate(python_files):
              for file2 in python_files[i + 1:]:
                  file1_path = os.path.join(question_path, file1)
                  file2_path = os.path.join(question_path, file2)
                  
                  # Read the code from both files
                  with open(file1_path, 'r', encoding='utf-8') as f1, open(file2_path, 'r', encoding='utf-8') as f2:
                      code1 = f1.read()
                      code2 = f2.read()
                  
                  file_pairs.append(((file1_path, code1), (file2_path, code2)))
      
      return file_pairs

    def compute_all(self, code1, code2):
        token_sim = self.token_sim.compute(code1, code2)
        ast_sim = self.ast_sim.compute(code1, code2)
        embed_sim = self.embed_sim.compute(code1, code2)
        return token_sim, ast_sim, embed_sim


# ===========================
#  Process Code Pairs
# ===========================
def process_code_pairs(file_pairs, pipeline):
    results = []

    def process_pair(pair):
        (file1, code1), (file2, code2) = pair
        token_sim, ast_sim, embed_sim = pipeline.compute_all(code1, code2)
        '''
        return {
            "file1": file1,
            "file2": file2,
            "token_sim": token_sim,
            "ast_sim": ast_sim,
            "embed_sim": embed_sim
        }
        '''

        return {
            "file1": file1,
            "file2": file2,
            "similarity_score": embed_sim
        }
    with ThreadPoolExecutor() as executor:
        for result in tqdm(executor.map(process_pair, file_pairs), total=len(file_pairs), desc="Processing pairs"):
            results.append(result)

    return results


# ===========================
#  Main Execution
# ===========================
if __name__ == "__main__":
    extraction_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'server'))
    sample_path = "files"
    # get the sample files in the sample
    sample_files = os.path.join(extraction_path, sample_path)
    sample_files = os.listdir(sample_files)

    file_pairs = []
    for i in range(len(sample_files)):
        for j in range(i + 1, len(sample_files)):
            file1_path = os.path.join(extraction_path, sample_path, sample_files[i])
            file2_path = os.path.join(extraction_path, sample_path, sample_files[j])
            with open(file1_path, 'r', encoding='utf-8') as f1, open(file2_path, 'r', encoding='utf-8') as f2:
                code1 = f1.read()
                code2 = f2.read()
            file_pairs.append(((sample_files[i], code1), (sample_files[j], code2)))
    model = "microsoft/codebert-base"
    pipeline = CodeSimilarityPipeline(model)
    results = process_code_pairs(file_pairs, pipeline)

    with open("../similarity_results.json", "w") as f:
        json.dump(results, f, indent=4)