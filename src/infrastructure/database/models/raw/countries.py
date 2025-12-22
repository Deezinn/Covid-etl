from sqlalchemy import Column, Integer, Float, BigInteger, String, JSON
from infrastructure.database.models.base import Base

class RawCountries(Base):
    __tablename__ = "raw_countries"

    id = Column(Integer, primary_key=True, autoincrement=True)

    # timestamp bruto da API (ms)
    updated = Column(BigInteger, nullable=True)

    country = Column(String, nullable=True)

    # objeto aninhado da API
    countryInfo = Column(JSON, nullable=True)

    cases = Column(Integer, nullable=True)
    todayCases = Column(Integer, nullable=True)

    deaths = Column(Integer, nullable=True)
    todayDeaths = Column(Integer, nullable=True)

    recovered = Column(Integer, nullable=True)
    todayRecovered = Column(Integer, nullable=True)

    active = Column(Integer, nullable=True)
    critical = Column(Integer, nullable=True)

    casesPerOneMillion = Column(Integer, nullable=True)
    deathsPerOneMillion = Column(Integer, nullable=True)

    tests = Column(Integer, nullable=True)
    testsPerOneMillion = Column(Integer, nullable=True)

    population = Column(Integer, nullable=True)

    continent = Column(String, nullable=True)

    oneCasePerPeople = Column(Integer, nullable=True)
    oneDeathPerPeople = Column(Integer, nullable=True)
    oneTestPerPeople = Column(Integer, nullable=True)

    activePerOneMillion = Column(Float, nullable=True)
    recoveredPerOneMillion = Column(Float, nullable=True)
    criticalPerOneMillion = Column(Integer, nullable=True)
