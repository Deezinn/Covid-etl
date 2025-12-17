import pandas as pd
from domain.interfaces import TransformBase


class Continents(TransformBase):
    pass

    def transform(self, data):
        dataframe = pd.DataFrame(data)
        return dataframe