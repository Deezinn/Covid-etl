from sqlalchemy import Column, Integer, Float, BigInteger, String, JSON
from infrastructure.database.models.base import Base

class RawContinents(Base):
    __tablename__ = "raw_continents"

    id = Column(Integer, primary_key=True)

    updated = Column(BigInteger)

    cases = Column(BigInteger)
    todayCases = Column(BigInteger)

    deaths = Column(BigInteger)
    todayDeaths = Column(BigInteger)

    recovered = Column(BigInteger)
    todayRecovered = Column(BigInteger)

    active = Column(BigInteger)
    critical = Column(BigInteger)

    casesPerOneMillion = Column(Float)
    deathsPerOneMillion = Column(Float)

    tests = Column(BigInteger)        
    testsPerOneMillion = Column(Float)

    population = Column(BigInteger)   

    continent = Column(String)

    activePerOneMillion = Column(Float)
    recoveredPerOneMillion = Column(Float)
    criticalPerOneMillion = Column(Float)

    continentInfo = Column(JSON)
    countries = Column(JSON)

