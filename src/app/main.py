from settings.constants import APISURL

from pipeline.extract import Extract
from pipeline.transform_pipeline import TransformPipeline
from pipeline.load import Load

from infrastructure.database.connections.loader import load_database_credentials
from infrastructure.database.connections.factory import create_database_url

from infrastructure.database.models.base import Base

from sqlalchemy import create_engine

class Pipeline:
    def __init__(self, extract: Extract, transformPipeline: TransformPipeline, Load):
        self.__extract = extract
        self.__transform_pipeline = transformPipeline
        self.__load = Load

    def run(self):
        data = self.__extract.get_data()

        raw_data, process_data = self.__transform_pipeline.execute(data)
        
        self.__load.load_raw(raw_data)
        self.__load.load_process(process_data)

if __name__ == "__main__":
    extract = Extract(APISURL)
    transform = TransformPipeline()
    
    credentials = load_database_credentials()
    url = create_database_url(credentials)
    engine = create_engine(url)
    Base.metadata.create_all(bind=engine)

    load = Load(engine)
    
    p = Pipeline(extract, transform, load)
    p.run()