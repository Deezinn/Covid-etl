from abc import ABC, abstractmethod


class TransformBase(ABC):
    """Interface base para classes de transformação"""
    pass
    
    @staticmethod
    @abstractmethod
    def _normalize(data):
        pass
    
    @staticmethod
    @abstractmethod
    def _validate_output(dataframe_process):
        pass

    @staticmethod
    @abstractmethod
    def _sanitize(data):
        pass
    
    @abstractmethod
    def transform(self, data):
        pass
    