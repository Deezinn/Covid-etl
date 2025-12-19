import pandas as pd
from domain.interfaces import TransformBase


class States(TransformBase):
    pass

    @staticmethod
    def _normalize(data):
        pass
    
    @staticmethod
    def _validate_output(dataframe_process):
        pass

    @staticmethod
    def _sanitize(data) -> pd.DataFrame:
        return pd.DataFrame(data)
    
    def transform(self, data) -> str:
        data_normalized = self._normalize(data)
        dataframe_normalized = self._sanitize(data_normalized)
        dataframe_validated = self._validate_output(dataframe_normalized)
        if dataframe_validated:
            return dataframe_validated.model_dump_json()