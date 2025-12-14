from domain.settings.constants import APISURL

from pipeline.extract import Extract
from pipeline.transform import Transform

class Pipeline:
    def __init__(self, extract: Extract, transform: Transform):
        self.__extract = extract
        self.__transform = transform

    def run(self):
        data = self.__extract.get_data()

        raw_data, process_data = self.__transform.orchestrator(data)
        
        print(raw_data)
        print(process_data)

if __name__ == "__main__":
    extract = Extract(APISURL)
    transform = Transform()
    
    p = Pipeline(extract, transform)
    p.run()
