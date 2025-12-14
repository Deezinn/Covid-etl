from dataclasses import dataclass
from typing import Optional


@dataclass
class Continents:
    updated: Optional[int] = None
    cases: Optional[int] = None
    todayCases: Optional[int] = None
    deaths: Optional[int] = None
    todayDeaths: Optional[int] = None
    recovered: Optional[int] = None
    todayRecovered: Optional[int] = None
    active: Optional[int] = None
    critical: Optional[int] = None
    casesPerOneMillion: Optional[float] = None
    deathsPerOneMillion: Optional[float] = None
    tests: Optional[int] = None
    testsPerOneMillion: Optional[float] = None
    population: Optional[int] = None
    continent: Optional[str] = None
    activePerOneMillion: Optional[float] = None
    recoveredPerOneMillion: Optional[float] = None
    criticalPerOneMillion: Optional[float] = None
    continentInfo: Optional[dict] = None
    countries: Optional[list] = None