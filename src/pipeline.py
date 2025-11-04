from .etl import Extract, TransformAll, TransformContinents, TransformCountries, TransformStates

import pandas as pd
from pandas import json_normalize

class Pipeline:
    def __init__(self):
        self.__extract = Extract()
        self.__transformAll = TransformAll()
        self.__tranformContinents = TransformContinents()
        self.__transformCountries = TransformCountries()
        self.__trasnformStates = TransformStates()
    
    def run(self):
        raw_data = self.__extract.get()
        raw_data_all = self.__transformAll.process(raw=raw_data['all'])
        raw_data_continents = self.__tranformContinents.process(raw=raw_data['continents'])
        raw_data_countries = self.__transformCountries.process(raw=raw_data['countries'])
        raw_data_states = self.__trasnformStates.process(raw=raw_data['states'])
        
        # print(raw_data_all.info())
        # print(raw_data_continents.info())
        # print(raw_data_countries.info())
        print(raw_data_states.info())

if __name__ == "__main__":
    p = Pipeline()
    p.run()