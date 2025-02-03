from abc import ABC, abstractmethod

class abstract_model(ABC):
    @abstractmethod
    def train(self, data: tuple[list[str], dict[str, float]], supervised: bool, timeout: int) -> None:
        pass

    @abstractmethod
    def predict(self, data: list[str])-> dict[str,float]:
        pass