from abstract_report_generation import abstract_report_generation
from v0_cosine_similarity import cosine_similarity as plagiarism
import json

class report_generation(abstract_report_generation):
    def generate(data):
        data = json.loads(data)
        plagiarism_matrix = plagiarism.score(data)
        data.update({'plagiarism_matrix': plagiarism_matrix.tolist()})
        results = report_generation._assemble_visuals(data)
        return results
    
    def _assemble_visuals(data):
        visuals = dict()
        visuals['plagiarism_matrix'] = data['plagiarism_matrix']
        visuals['threshold'] = data['threshold']
        visuals = json.dumps(visuals)
        return visuals
        
