from transform.transformCovid import DataTransform
from pymongo import MongoClient


class LoadData:
    def __init__(self) -> None:
        self.datatransform = DataTransform()
        self.mongoclient = MongoClient("mongodb+srv://admin:admin@cluster0.yzcpftc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        self.db = self.mongoclient["covid-data"]
        self.collection = self.db["paises-covid"]

    def load_to_mongo(self):
        dados_traduzidos = self.datatransform.traduzir_chaves()
        for i in range(len(dados_traduzidos)):
            inserted = self.collection.insert_one(dados_traduzidos[i])
            print(f"Inserted ID: {inserted.inserted_id}")

if __name__ == "__main__":
    loader = LoadData()
    loader.load_to_mongo()
