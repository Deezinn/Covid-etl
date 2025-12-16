from dataclasses import dataclass
from typing import Optional


@dataclass
class AllCasesDTO:
    updated: Optional[int] = None
    cases: Optional[int] = None
    todayCases: Optional[int] = None
    deaths: Optional[int] = None
    todayDeaths: Optional[int] = None
    recovered: Optional[int] = None
    todayRecovered: Optional[int] = None
    active: Optional[int] = None
    critical: Optional[int] = None
    casesPerOneMillion: Optional[int] = None
    deathsPerOneMillion: Optional[float] = None
    tests: Optional[int] = None
    testsPerOneMillion: Optional[float] = None
    population: Optional[int] = None
    oneCasePerPeople: Optional[int] = None
    oneDeathPerPeople: Optional[int] = None
    oneTestPerPeople: Optional[int] = None
    activePerOneMillion: Optional[float] = None
    recoveredPerOneMillion: Optional[float] = None
    criticalPerOneMillion: Optional[float] = None
    affectedCountries: Optional[int] = None
