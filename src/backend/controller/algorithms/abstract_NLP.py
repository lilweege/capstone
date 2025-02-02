from abc import ABC, abstractmethod
import abstract_tokenizer
import abstract_AST
import abstract_model
import json


class abstract_NLP(ABC):
    @abstractmethod
    def combinedPredict(data: json) -> list[dict[str, float]]:
        pass