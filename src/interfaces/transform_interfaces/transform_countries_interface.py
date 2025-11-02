from abc import ABC, abstractmethod

class TransformCountriesInterface(ABC):
    @abstractmethod
    def process(self, raw: str):
        """Recebe o conjunto de dados em json e transforma em dataframe"""
        pass
