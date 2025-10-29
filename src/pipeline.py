from .etl import Extract, TransformAll, TransformContinents

import pandas as pd
from pandas import json_normalize

class Pipeline:
    def __init__(self):
        self.__extract = Extract()
        self.__transformAll = TransformAll()
        self.__tranformContinents = TransformContinents()
    
    def run(self):
        raw_data = self.__extract.get()
        raw_data_all = self.__transformAll.process(raw=raw_data['all'])
        raw_data_continents = self.__tranformContinents.process(raw=raw_data['continents'])
        print(raw_data_continents.info())
        

if __name__ == "__main__":
    p = Pipeline()
    p.run()