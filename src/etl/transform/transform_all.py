import pandas as pd
from src.interfaces import TransformAllInterface


class TransformAll(TransformAllInterface):
    def __init__(self):
        self._raw_dataframe = None
        
    
    def process(self, raw: str):
        """Recebe o conjunto de dados em json e transforma em dataframe"""
    
        raw_data_normalized = pd.json_normalize(raw)
        self._raw_dataframe = pd.DataFrame(raw_data_normalized)
        self.transform_orquestrador()
        return self._raw_dataframe
    
    def transform_orquestrador(self):
        self._translate_columns()
        self._convert_types()
        self._sanitize_columns()
    
    def _translate_columns(self):
        colunas_traducao = {
            "updated": "atualizado_em",
            "cases": "casos_total",
            "todayCases": "casos_hoje",
            "deaths": "mortes_total",
            "todayDeaths": "mortes_hoje",
            "recovered": "recuperados_total",
            "todayRecovered": "recuperados_hoje",
            "active": "casos_ativos",
            "critical": "casos_críticos",
            "casesPerOneMillion": "casos_por_milhão",
            "deathsPerOneMillion": "mortes_por_milhão",
            "tests": "testes_total",
            "testsPerOneMillion": "testes_por_milhão",
            "population": "população",
            "oneCasePerPeople": "um_caso_por_pessoas",
            "oneDeathPerPeople": "uma_morte_por_pessoas",
            "oneTestPerPeople": "um_teste_por_pessoas",
            "activePerOneMillion": "ativos_por_milhão",
            "recoveredPerOneMillion": "recuperados_por_milhão",
            "criticalPerOneMillion": "críticos_por_milhão",
            "affectedCountries": "países_afetados"
        }

        self._raw_dataframe = self._raw_dataframe.rename(columns=colunas_traducao)
    
    def _convert_types(self):
        """Converte colunas para tipos ideais (int16, int32, int64, float32, datetime)."""
        self._raw_dataframe['atualizado_em'] = pd.to_datetime(self._raw_dataframe['atualizado_em'], unit='ms')
        
        columns_to_transform_int32 = ['casos_total', 'casos_hoje', 'mortes_total', 'recuperados_total', 'casos_ativos', 'casos_críticos']
        for coluna in columns_to_transform_int32:
            self._raw_dataframe[coluna] = self._raw_dataframe[coluna].astype('int32')
            
        columns_to_transform_float32 = ['casos_por_milhão','mortes_por_milhão', 'testes_por_milhão', 'ativos_por_milhão', 'recuperados_por_milhão','críticos_por_milhão']
        for coluna in columns_to_transform_float32:
            self._raw_dataframe[coluna] = self._raw_dataframe[coluna].astype('float32')
            
        columns_to_transform_int64 = ['testes_total','população', 'países_afetados']
        for coluna in columns_to_transform_int64:
            self._raw_dataframe[coluna] = self._raw_dataframe[coluna].astype('int64')

        columns_to_transform_int16 = ['recuperados_hoje', 'um_caso_por_pessoas', 'uma_morte_por_pessoas']
        for coluna in columns_to_transform_int16:
            self._raw_dataframe[coluna] = self._raw_dataframe[coluna].astype('int16')
        
    def _sanitize_columns(self):
        """Trata valores ausentes e inconsistências nas colunas."""
        for coluna in self._raw_dataframe.columns:
            self._raw_dataframe[coluna].fillna(0, inplace=True)
        
        