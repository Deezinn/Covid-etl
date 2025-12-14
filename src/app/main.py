from settings.constants import APISURL

from pipeline.extract import Extract
from pipeline.transform_pipeline import TransformPipeline

class Pipeline:
    def __init__(self, extract: Extract, transform: TransformPipeline):
        self.__extract = extract
        self.__transform = transform

    def run(self):
        data = self.__extract.get_data()

        raw_data, process_data = self.__transform.execute(data)
        # print(raw_data, process_data)
        

if __name__ == "__main__":
    extract = Extract(APISURL)
    transform = TransformPipeline()
    
    p = Pipeline(extract, transform)
    p.run()
