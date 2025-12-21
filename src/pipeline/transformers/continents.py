import ast
import pandas as pd
import numpy as np

from domain.interfaces import TransformBase
from domain.utils import cleanList
from domain.dtos import ContinentsDTO

from infrastructure.database.schemas import ContinentsSchema


class Continents(TransformBase):
    pass

    @staticmethod
    def _normalize(data):
        return [ContinentsDTO(**dados) for dados in data]
    
    @staticmethod
    def _validate_output(dataframe_process):
        return [ContinentsSchema(**dados) for dados in dataframe_process.to_dict(orient='records')]

    @staticmethod
    def _sanitize(data) -> pd.DataFrame:
        
        column_translate = {
            'updated': 'ultima_atualizacao',
            'cases': 'casos_totais',
            'todayCases': 'casos_hoje',
            'deaths': 'obitos_totais',
            'todayDeaths': 'obitos_hoje', 
            'recovered': 'recuperados',
            'todayRecovered': 'recuperados_hoje', 
            'active': 'casos_ativos', 
            'critical': 'casos_criticos', 
            'casesPerOneMillion': 'casos_por_milhao_habitantes',
            'deathsPerOneMillion': 'obitos_por_milhao_habitantes', 
            'tests': 'total_testes', 
            'testsPerOneMillion': 'testes_por_milhao_habitantes',
            'population': 'populacao_total', 
            'continent': 'continente', 
            'activePerOneMillion': 'casos_ativos_por_milhao_habitantes',
            'recoveredPerOneMillion': 'recuperados_por_milhao_habitantes',
            'criticalPerOneMillion': 'criticos_por_milhao_habitantes',
            'continentInfo': 'continente_info',
            'countries': 'paises'
        }
        
        dataframe_column_types = {
            'ultima_atualizacao': 'int64',
            'casos_totais': 'int32',
            'casos_hoje': 'int32',
            'obitos_totais': 'int32',
            'obitos_hoje': 'int32',
            'recuperados': 'int32',
            'recuperados_hoje': 'int32',
            'casos_ativos': 'int32',
            'casos_criticos':'int32',
            'casos_por_milhao_habitantes': 'float32',
            'obitos_por_milhao_habitantes': 'float32',
            'total_testes': 'int64',
            'testes_por_milhao_habitantes': 'float32',
            'populacao_total': 'int32',
            'continente': 'str',
            'casos_ativos_por_milhao_habitantes': 'float32',
            'recuperados_por_milhao_habitantes': 'float32',
            'criticos_por_milhao_habitantes': 'float32',
            'continente_info': 'str',
            'paises': 'object'
        }
        
        rename_continente = {
            'North America': 'América do Norte',
            'Asia': 'Ásia',
            'Europe': 'Europa',
            'South America': 'América do Sul',
            'Australia-Oceania': 'Oceania',
            'Africa': 'África'
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
        
        dataframe = pd.DataFrame(data)
        
        dataframe = dataframe.rename(columns=column_translate)
        
        dataframe = dataframe.astype(dataframe_column_types)
        
        dataframe['ultima_atualizacao'] = pd.to_datetime(arg=dataframe['ultima_atualizacao'], unit='ns', utc=True)
        
        for coluna in dataframe.select_dtypes(['object']).columns:
            if coluna == 'paises':
                dataframe[coluna] = dataframe[coluna].apply(
                    cleanList
                )
            else:
                dataframe[coluna] = (dataframe[coluna]
                         .astype('str')
                         .str.
                         strip().
                         str.title())
            
            if coluna == 'continente':
                dataframe[coluna] = dataframe[coluna].replace(rename_continente)
            
            if coluna == 'continente_info':
                dataframe[coluna] =  dataframe[coluna].apply(
                    lambda x: ast.literal_eval(x) if isinstance(x, str) else x
                )
                
        dataframe['continente_info'] =  dataframe['continente_info'].apply(
            lambda x: ast.literal_eval(x) if isinstance(x, str) else x
        )

        dataframe['continente_lat'] = dataframe['continente_info'].apply(
            lambda x: x.get('Lat')
        )

        dataframe['continente_long'] = dataframe['continente_info'].apply(
            lambda x: x.get('Long')
        )
        
        if 'continente_lat' and 'continente_long' in dataframe.columns:
            del dataframe['continente_info']
        
        for coluna in dataframe.select_dtypes(['int', 'float']).columns:
            dataframe[coluna] = (
                dataframe[coluna]
                .clip(lower=0)
                .replace(possible_missing_values, 0)
                .fillna(0)
            )
        dataframe.to_csv('../csv/continents.csv')
        return dataframe
    
    def transform(self, data) -> list[dict]:
        data_normalized = self._normalize(data)
        dataframe_normalized = self._sanitize(data_normalized)
        dataframe_validated = self._validate_output(dataframe_normalized)
        return [data_dump.model_dump() for data_dump in dataframe_validated]
        
        