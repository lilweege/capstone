from abc import ABC, abstractmethod
from typing_extensions import Self

class abstract_AST(ABC): #throws invalidSyntaxException
    @abstractmethod
    def parse(self, rawSource: str) -> Self: #AST object return
        pass