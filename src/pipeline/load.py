from sqlalchemy import create_engine

class Load:
    def __init__(self, engine):
        self.__engine = engine

     
    def create_connection(self):
       with self.__engine.begin() as conn:
           print('conexao feita com sucesso')