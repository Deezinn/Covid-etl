import pandas as pd
from domain.interfaces import TransformBase


class States(TransformBase):
    pass

    def transform(self, data):
        dataframe = pd.DataFrame(data)
        return dataframe