import pandas as pd
from domain.interfaces import TransformInterface

class Transform(TransformInterface):
    def __init__(self):
        pass
    
    def orchestrator(self, datasets):
        raw_data = {}
        process_data = {}
         
        for key, data in datasets.items():
            raw_data[key] = data
            match key:
                case 'all':
                    process_data[key] = self._transform_all(data)
                case 'states':
                    process_data[key] = self._transform_states(data)
                case 'continents':
                    process_data[key] = self._transform_continents(data)
                case 'countries':
                    process_data[key] = self._trasnform_countries(data)
                case _:
                    pass
                
        return raw_data, process_data
    
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