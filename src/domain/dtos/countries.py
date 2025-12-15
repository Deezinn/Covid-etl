from dataclasses import dataclass
from typing import Optional


@dataclass
class Countries:
    updated: Optional[int] = None
    country: Optional[str] = None
    countryInfo: Optional[dict] = None
    cases: Optional[int] = None
    todayCases: Optional[int] = None
    deaths: Optional[int] = None
    todayDeaths: Optional[int] = None
    recovered: Optional[int] = None
    todayRecovered: Optional[int] = None
    active: Optional[int] = None
    critical: Optional[int] = None
    casesPerOneMillion: Optional[int] = None
    deathsPerOneMillion: Optional[int] = None
    tests: Optional[int] = None
    testsPerOneMillion: Optional[int] = None
    population: Optional[int] = None
    continent: Optional[str] = None
    oneCasePerPeople: Optional[int] = None
    oneDeathPerPeople: Optional[int] = None
    oneTestPerPeople: Optional[int] = None
    activePerOneMillion: Optional[float] = None
    recoveredPerOneMillion: Optional[float] = None
    criticalPerOneMillion: Optional[int] = None