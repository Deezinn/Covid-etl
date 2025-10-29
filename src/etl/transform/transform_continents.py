import pandas as pd
from src.interfaces import TransformContinentsInterface


class TransformContinents(TransformContinentsInterface):
    def __init__(self):
        self._raw_dataframe = None
        
    def process(self, raw: str):
        """Recebe o conjunto de dados em json e transforma em dataframe"""
    
        raw_data_normalized = pd.json_normalize(raw)
        self._raw_dataframe = pd.DataFrame(raw_data_normalized)
        
        # self._transform_orquestrador()
        return self._raw_dataframe