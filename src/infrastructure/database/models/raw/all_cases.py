from sqlalchemy import Column, Integer, Float, BigInteger
from infrastructure.database.models.base import Base


class RawAllCases(Base):
    __tablename__ = "raw_all_cases"

    id = Column(Integer, primary_key=True, autoincrement=True)

    # timestamp bruto da API (ms)
    updated = Column(BigInteger, nullable=True)

    # contadores globais (podem ultrapassar 2bi)
    cases = Column(BigInteger, nullable=True)
    todayCases = Column(BigInteger, nullable=True)

    deaths = Column(BigInteger, nullable=True)
    todayDeaths = Column(BigInteger, nullable=True)

    recovered = Column(BigInteger, nullable=True)
    todayRecovered = Column(BigInteger, nullable=True)

    active = Column(BigInteger, nullable=True)
    critical = Column(BigInteger, nullable=True)

    # métricas por milhão
    casesPerOneMillion = Column(Float, nullable=True)
    deathsPerOneMillion = Column(Float, nullable=True)

    tests = Column(BigInteger, nullable=True)
    testsPerOneMillion = Column(Float, nullable=True)

    population = Column(BigInteger, nullable=True)

    # proporções inteiras
    oneCasePerPeople = Column(BigInteger, nullable=True)
    oneDeathPerPeople = Column(BigInteger, nullable=True)
    oneTestPerPeople = Column(BigInteger, nullable=True)

    # métricas por milhão
    activePerOneMillion = Column(Float, nullable=True)
    recoveredPerOneMillion = Column(Float, nullable=True)
    criticalPerOneMillion = Column(Float, nullable=True)

    affectedCountries = Column(Integer, nullable=True)
