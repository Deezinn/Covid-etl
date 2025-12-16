from abc import ABC, abstractmethod


class TransformBase(ABC):
    """Interface base para classes de transformação"""
    pass
    
    @abstractmethod
    def transform(self, data):
        """Aplica transformação nos dados extraídos

        Args:
            data (dict): Dados brutos da etapa de extração

        Returns:
            dict: Dados transformados
        """
        pass