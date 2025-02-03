from abc import ABC, abstractmethod
import json
from abstract_similarity_score import abstract_similarity_score

class abstract_report_generation(ABC):
    @abstractmethod
    def generate(data: json) -> json:
        pass

    @abstractmethod
    def _assemble_visuals(data: json) -> json:
        pass