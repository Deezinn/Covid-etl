import pandas as pd
from src.interfaces import TransformStatesInterface


class TransformStates(TransformStatesInterface):
    def __init__(self):
        self._raw_dataframe = None
        
    def process(self, raw: str):
        """Recebe o conjunto de dados em json e transforma em dataframe"""
    
        raw_data_normalized = pd.json_normalize(raw)
        self._raw_dataframe = pd.DataFrame(raw_data_normalized)
        
        self._transform_orquestrador()
        return self._raw_dataframe
    
    def _transform_orquestrador(self):
        self._translate_columns()
        self._convert_types()
        self._sanitize_columns()
    
    def _translate_columns(self):
        traducao_dict = {
            "state": "estados",
            "updated": "atualizado",
            "cases": "casos",
            "deaths": "óbitos",
            "recovered": "recuperados",
            "casesPerOneMillion": "casosPorMilhão",
            "deathsPerOneMillion": "óbitosPorMilhão",
            "population": "população",
            "object": "texto",
            "int64": "inteiro"
        }

        self._raw_dataframe = self._raw_dataframe.rename(columns=traducao_dict)

    def _convert_types(self):
        for coluna in self._raw_dataframe.columns:
            match coluna:
                case 'estados':
                   self._raw_dataframe[coluna] = self._raw_dataframe[coluna].astype(str)
                case 'atualizado':
                    self._raw_dataframe[coluna] = pd.to_datetime(self._raw_dataframe[coluna], unit='ms')
                case 'óbitos' | 'casos' | 'recuperados' | 'casosPorMilhão' | 'população':
                    self._raw_dataframe[coluna] = self._raw_dataframe[coluna].astype("Int32")
                case 'óbitosPorMilhão':
                    self._raw_dataframe[coluna] = self._raw_dataframe[coluna].astype("Int16")
                case _:
                    print(f"Coluna inválida {coluna}")
        
    def _sanitize_columns(self):
        for coluna in self._raw_dataframe.columns:
            match coluna:
                case 'estados':
                   self._raw_dataframe[coluna] = self._raw_dataframe[coluna].fillna('Não informado')
                case 'atualizado':
                    self._raw_dataframe[coluna] = self._raw_dataframe[coluna].fillna(pd.NaT)
                case 'óbitos' | 'casos' | 'recuperados' | 'casosPorMilhão' | 'óbitosPorMilhão' | 'população':
                    self._raw_dataframe[coluna] = self._raw_dataframe[coluna].fillna(0)
                case _:
                    print(f"Coluna inválida {coluna}")
        
                