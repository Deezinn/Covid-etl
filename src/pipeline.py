from .etl import Extract, TransformAll

import pandas as pd
from pandas import json_normalize

class Pipeline:
    def __init__(self):
        self.__extract = Extract()
        self.__transformAll = TransformAll()
    
    def run(self):
        raw_data = self.__extract.get()
        raw_data_all = self.__transformAll.process(raw=raw_data['all'])
        

if __name__ == "__main__":
    p = Pipeline()
    p.run()