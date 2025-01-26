from app.similarity import TokenSimilarity, ASTSimilarity, EmbeddingSimilarity

class CodeSimilarityPipeline:
    def __init__(self, model_name="microsoft/codebert-base"):
        self.token_sim = TokenSimilarity()
        self.ast_sim = ASTSimilarity()
        self.embed_sim = EmbeddingSimilarity(model_name)

    def compute_all(self, code1, code2):
        """Compute similarity scores using all three methods."""
        token_sim = self.token_sim.compute(code1, code2)
        ast_sim = self.ast_sim.compute(code1, code2)
        embed_sim = self.embed_sim.compute(code1, code2)
        return {"token_sim": token_sim, "ast_sim": ast_sim, "embed_sim": embed_sim}
