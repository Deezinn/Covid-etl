from .etl import Extract

import pandas as pd
from pandas import json_normalize

class Pipeline:
    def __init__(self):
        self.__extract = Extract()
    
    def run(self):
        json_data = self.__extract.get()
        
        for endpoint,json in json_data.items():
            jsn = json_normalize(json)
            df = pd.DataFrame(jsn)
            df.to_csv(f'data/{endpoint}.csv')

if __name__ == "__main__":
    p = Pipeline()
    p.run()