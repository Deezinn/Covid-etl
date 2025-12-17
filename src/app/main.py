from settings.constants import APISURL

from pipeline.extract import Extract
from pipeline.transform_pipeline import TransformPipeline

from infrastructure.database.security import ENVDATABASE

class Pipeline:
    def __init__(self, extract: Extract, transformPipeline: TransformPipeline):
        self.__extract = extract
        self.__transform_pipeline = transformPipeline

    def run(self):
        data = self.__extract.get_data()

        raw_data, process_data = self.__transform_pipeline.execute(data)
        print(ENVDATABASE)
        

if __name__ == "__main__":
    extract = Extract(APISURL)
    transform = TransformPipeline()
    
    p = Pipeline(extract, transform)
    p.run()
