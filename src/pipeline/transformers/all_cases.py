import numpy as np
import pandas as pd

from domain.interfaces import TransformBase
from domain.dtos import AllCasesDTO

from infrastructure.database.schemas import AllCasesSchema

class AllCases(TransformBase):

    @staticmethod
    def _normalize(data) -> AllCasesDTO:
        return AllCasesDTO(**data)
    
    @staticmethod
    def _validate_output(dataframe_process):
        return AllCasesSchema(**dataframe_process.to_dict('records')[0])

    @staticmethod
    def _sanitize(data) -> pd.DataFrame:

        translate_columns = { "updated":"ultima_atualizacao",
            "cases":"casos_totais",
            "todayCases":"casos_hoje",     
            "deaths":"obitos_totais",
            "todayDeaths":"obitos_hoje", 
            "recovered":"recuperados_totais",
            "todayRecovered":"recuperados_hoje",      
            "active":"casos_ativos",
            "critical":"casos_criticos",     
            "casesPerOneMillion":"casos_por_milhao_habitantes", 
            "deathsPerOneMillion":"obitos_por_milhao_habitantes",       
            "tests":"total_testes",        
            "testsPerOneMillion":"testes_por_milhao_habitantes",
            "population":"populacao_total",    
            "oneCasePerPeople": "uma_pessoa_por_caso",    
            "oneDeathPerPeople":"uma_pessoa_por_obito",    
            "oneTestPerPeople": "uma_pessoa_por_teste",  
            "activePerOneMillion": "casos_ativos_por_milhao_habitantes",  
            "recoveredPerOneMillion":"recuperados_por_milhao_habitantes", 
            "criticalPerOneMillion":"criticos_por_milhao_habitantes",     
            "affectedCountries":"numero_paises_afetados"  
        }      
        
        transform_type = {
            'ultima_atualizacao': 'int64',
            'recuperados_totais': 'int64',
            'total_testes': 'int64',
            'populacao_total': 'int64',

            'casos_totais': 'int64',
            'obitos_totais': 'int64',
            'casos_ativos': 'int64',
            'casos_criticos': 'int32',

            'casos_hoje': 'int32',
            'obitos_hoje': 'int32',
            'recuperados_hoje': 'int32',

            'casos_por_milhao_habitantes': 'float32',
            'obitos_por_milhao_habitantes': 'float32',
            'testes_por_milhao_habitantes': 'float64',

            'casos_ativos_por_milhao_habitantes': 'float32',
            'recuperados_por_milhao_habitantes': 'float32',
        }
        
        possible_missing_values = [
            '', ' ', '  ',
            'null', 'NULL',
            'none', 'None', 'NONE',
            'undefined', 'UNDEFINED',
            'nan', 'NaN', 'NAN',
            'na', 'NA',
            'n/a', 'N/A',
            '#N/A',
            '-', '--', '---',
            '?', '??',
            None, pd.NA, np.nan
        ]
        
        dataframe = pd.DataFrame([data])
        
        dataframe = dataframe.rename(columns=translate_columns)
        
        dataframe = dataframe.astype(transform_type)
        
        dataframe = dataframe.replace(possible_missing_values, 0)
        
        dataframe['ultima_atualizacao'] = pd.to_datetime(
            dataframe['ultima_atualizacao'],
            unit='ns',
            utc=True
        )
        
        numeric_columns = dataframe.select_dtypes(include=['int', 'float']).columns
        
        dataframe[numeric_columns] = dataframe[numeric_columns].apply(pd.to_numeric, errors='coerce').fillna(0)
        
        dataframe[numeric_columns] = dataframe[numeric_columns].clip(lower=0)

        return dataframe 

    def transform(self, data) -> str:
        data_normalized = self._normalize(data)
        dataframe_normalized = self._sanitize(data_normalized)
        dataframe_validated = self._validate_output(dataframe_normalized)
        return dataframe_validated.model_dump_json()
    