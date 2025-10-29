from abc import ABC, abstractmethod

class TransformContinentsInterface(ABC):
    @abstractmethod
    def process(self, raw: str):
        """Recebe o conjunto de dados em json e transforma em dataframe"""
        pass
