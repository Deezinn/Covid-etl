import pandas as pd
from domain.interfaces import TransformInterface

class Transform(TransformInterface):
    def __init__(self):
        pass
    
    def orchestrator(self, datasets):
        bronze = {}
        gold = {}
         
        for key, raw_data in datasets.items():
            bronze[key] = raw_data
            match key:
                case 'all':
                    gold[key] = self._transform_all(raw_data)
                case 'states':
                    gold[key] = self._transform_states(raw_data)
                case 'continents':
                    gold[key] = self._transform_continents(raw_data)
                case 'countries':
                    gold[key] = self._trasnform_countries(raw_data)
                case _:
                    pass
                
        return datasets, datasets
    
    @staticmethod
    def _transform_all(raw_data):
        dataframe = pd.DataFrame([raw_data])
        dataframe.to_csv('../csv/covid_all.csv')
        return dataframe
    
    @staticmethod
    def _transform_states(raw_data):
        dataframe = pd.DataFrame(raw_data)
        dataframe.to_csv('../csv/covid_states.csv')
        return dataframe
    
    @staticmethod
    def _transform_continents(raw_data):
        dataframe = pd.DataFrame(raw_data)
        dataframe.to_csv('../csv/covid_continents.csv')
        return dataframe
    
    @staticmethod
    def _trasnform_countries(raw_data):
        dataframe = pd.DataFrame(raw_data)
        dataframe.to_csv('../csv/covid_countries.csv')
        return dataframe