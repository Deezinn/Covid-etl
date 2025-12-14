import pandas as pd
from domain.interfaces import TransformPipelineInterface

from .transformers import AllCases, States, Continents, Countries

class TransformPipeline(TransformPipelineInterface):
    def __init__(self):
        self.__registry = {
            'all_cases' : AllCases(),
            'continents' : Continents(),
            'countries' : Countries(),
            'states' : States()
        }
    
    def execute(self, datasets):
        raw_data = {}
        process_data = {}
         
        for key, data in datasets.items():
            raw_data[key] = data
            if self.__registry[key] is not None:
                process_data[key] = self.__registry[key].transform(data=data)
        
        return raw_data, process_data
    