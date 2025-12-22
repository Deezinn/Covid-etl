from abc import ABC, abstractmethod


class LoadInterface(ABC):
    """Classe que servirá como modelo da carga dos dados"""
    pass
    
    @abstractmethod
    def load_raw(self, raw):
        pass
    
    @abstractmethod
    def load_process(self, process):
        pass