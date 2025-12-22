from infrastructure.database.models.raw import RawAllCases,RawContinents,RawCountries
from infrastructure.database.models.process import ProcessedAllCases, ProcessedContinents, ProcessedCountries

from sqlalchemy import insert

class Load:
    def __init__(self, engine):
        self.__engine = engine

    def load_raw(self, raw):
        schema_raw = {
            'all_cases': RawAllCases,
            'continents': RawContinents,
            'countries': RawCountries
        }


        with self.__engine.begin() as conn:
            for key, values in raw.items():
                if key not in schema_raw:
                    continue

                stmt = insert(schema_raw[key])
               
                if isinstance(values, dict):
                    conn.execute(stmt, [values])
                
                if isinstance(values,list):
                    conn.execute(stmt, values)
    
    def load_process(self, process):
        schema_process = {
            'all_cases': ProcessedAllCases,
            'continents': ProcessedContinents,
            'countries': ProcessedCountries
        }

        with self.__engine.begin() as conn:
            for key, values in process.items():
                if key not in schema_process:
                    continue

                stmt = insert(schema_process[key])
               
                if isinstance(values, dict):
                    conn.execute(stmt, values)
                
                if isinstance(values,list):
                    conn.execute(stmt, values)
    