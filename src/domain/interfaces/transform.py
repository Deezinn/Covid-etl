from abc import ABC, abstractmethod, abstractstaticmethod


class TransformInterface(ABC):
    
    @abstractmethod
    def orchestrator(self, datasets):
        pass
    
    @abstractmethod
    def _transform_all(raw_data):
        pass
    
    @abstractmethod
    def _transform_states(raw_data):
        pass
    
    @abstractmethod
    def _transform_continents(raw_data):
        pass
    
    @abstractmethod
    def _trasnform_countries(raw_data):
        pass