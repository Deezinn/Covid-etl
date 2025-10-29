from abc import ABC, abstractmethod

class TransformAllInterface(ABC):
    @abstractmethod
    def process(self, raw: str):
        """Recebe o conjunto de dados em json e transforma em dataframe"""
        pass

    @abstractmethod
    def _convert_types(self):
        """Converte colunas para tipos ideais (int16, int32, int64, float32, datetime)."""
        pass

    @abstractmethod
    def _sanitize_columns(self):
        """Trata valores ausentes e inconsistências nas colunas."""
        pass

    @abstractmethod
    def _translate_columns(self):
        """Tradução de colunas do dataset para nomes amigáveis em português"""
        pass
