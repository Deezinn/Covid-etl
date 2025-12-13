from domain.settings.constants import APISURL
from pipeline.extract import Extract


class Pipeline:
    def __init__(self, extract: Extract):
        self.__extract = extract

    def run(self):
        data = self.__extract.get_data()
        print(data)

if __name__ == "__main__":
    extract = Extract(APISURL)
    p = Pipeline(extract)
    p.run()
