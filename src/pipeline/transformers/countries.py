import ast
import pandas as pd
import numpy as np

from domain.interfaces import TransformBase
from domain.dtos import CountriesDTO

from infrastructure.database.schemas import CountriesSchema


class Countries(TransformBase):
    pass

    @staticmethod
    def _normalize(data):
        return [CountriesDTO(**registros) for registros in data]
    
    @staticmethod
    def _validate_output(dataframe_process):
        return [CountriesSchema(**registro_processado) for registro_processado in dataframe_process.to_dict(orient='records')]
    @staticmethod
    def _sanitize(data) -> pd.DataFrame:
        
        translate_columns = {
            'updated': 'ultima_atualizacao',
            'country': 'pais',
            'countryInfo': 'pais_info', 
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
            'oneCasePerPeople': 'pessoas_por_caso',
            'oneDeathPerPeople': 'pessoas_por_obito',
            'oneTestPerPeople': 'pessoas_por_teste',
            'activePerOneMillion': 'casos_ativos_por_milhao_habitantes',
            'recoveredPerOneMillion': 'recuperados_por_milhao_habitantes',
            'criticalPerOneMillion': 'criticos_por_milhao_habitantes'
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
            'casos_criticos': 'int32',
            'casos_por_milhao_habitantes': 'int32',
            'obitos_por_milhao_habitantes': 'int32',
            'total_testes': 'int32',
            'testes_por_milhao_habitantes': 'int32',
            'populacao_total': 'int32', 
            'pessoas_por_caso': 'int32',
            'pessoas_por_obito': 'int32', 
            'pessoas_por_teste': 'int32',
            'casos_ativos_por_milhao_habitantes': 'float64',
            'recuperados_por_milhao_habitantes': 'float64',
            'criticos_por_milhao_habitantes': 'float64',
            'pais': 'object',
            'pais_info': 'object', 
            'continente': 'object'
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
        
        continents_translate = {
            'Asia': "Ásia", 
            'Europe': 'Europa', 
            'Africa': 'África', 
            'North America': 'América do Norte',
            'South America': 'América do Sul',
            'Australia-Oceania ': 'Oceania'
        }
        
        extrair_colunas = ['Iso2', 'Iso3', 'Lat', 'Long']
        
        dataframe = pd.DataFrame(data)
        
        dataframe = dataframe.rename(columns=translate_columns)
        
        dataframe = dataframe.astype(dataframe_column_types)
        
        for coluna in dataframe.select_dtypes(['int', 'float']).columns:
            dataframe[coluna] = (
                dataframe[coluna]
                .clip(lower=0)
                .replace(possible_missing_values, 0)
                .fillna(0)
            )
            
            if coluna == 'ultima_atualizacao':
                dataframe[coluna] = pd.to_datetime(dataframe[coluna], unit='ms', utc=True, errors='coerce')
        
        for coluna in dataframe.select_dtypes(['object']).columns:
            dataframe[coluna] = (
                dataframe[coluna]
                .replace(possible_missing_values, 'Não Informado')
                .fillna('Não Informado')
                .astype('str')
                .str.strip()
                .str.title()
            )
            
            if coluna == 'continente':
                dataframe[coluna].replace(continents_translate)
            
            if coluna == 'pais_info':
                dataframe['pais_info'] = dataframe['pais_info'].apply(
                    lambda x: ast.literal_eval(x) if isinstance(x, str) else x
                )
            
        for coluna in extrair_colunas:
            dataframe[coluna] = dataframe['pais_info'].apply(
            lambda x: x.get(coluna)
        )
        
        mask_invalidos_cases = dataframe['casos_criticos'] > dataframe['casos_ativos']        
        dataframe = dataframe[~mask_invalidos_cases]

        mask_invalidos_tests = dataframe['total_testes'] < dataframe['casos_totais']
        dataframe = dataframe[~mask_invalidos_tests]
        
        
        extracao_ok = all(col in dataframe.columns for col in extrair_colunas)
                
        if extracao_ok and 'pais_info' in dataframe.columns:
            dataframe.drop(columns=['pais_info'], inplace=True)
            
        return dataframe
    
    def transform(self, data) -> list[object]:
        data_normalized = self._normalize(data)
        dataframe_normalized = self._sanitize(data_normalized)
        dataframe_validated = self._validate_output(dataframe_normalized)
        return [dados_validados.model_dump() for dados_validados in dataframe_validated]