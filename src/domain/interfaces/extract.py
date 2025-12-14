from abc import ABC, abstractmethod

class ExtractInterface(ABC):
    pass

    @abstractmethod
    def get_data(self):
        """
        Método que irá extrair os dados da api
        """
        
