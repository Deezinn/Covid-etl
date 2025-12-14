from abc import ABC, abstractmethod


class TransformPipelineInterface(ABC):
    """Classe que servirá como modelo de uma orquestração de transformação"""
    
    @abstractmethod
    def execute(self, datasets):
        """_summary_

        Args:
            datasets (json | dict): Dados puro da extração.
        """
    