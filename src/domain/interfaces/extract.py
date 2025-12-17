from abc import ABC, abstractmethod

class ExtractInterface(ABC):
    """Classe que servirá como modelo da extração dos dados"""
    pass

    @abstractmethod
    def get_data(self):
        """
        Método que irá extrair os dados da api
        """
        pass
        
