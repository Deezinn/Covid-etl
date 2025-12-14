import pandas as pd
from domain.interfaces import TransformInterface

from .transformers import AllCases, States, Continents, Countries

class TransformPipeline():
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
            
            if self.__registry[key] is not None and self.__registry:
                process_data[key] = self.__registry[key].transform(data=data)
                
        return raw_data, process_data
    