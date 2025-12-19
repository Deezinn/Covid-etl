from dataclasses import dataclass
from typing import Optional

@dataclass
class States:
    state: Optional[str] = None 
    updated: Optional[int] = None
    cases: Optional[int] = None
    deaths: Optional[int] = None 
    recovered: Optional[int] = None 
    casesPerOneMillion: Optional[int] = None 
    deathsPerOneMillion: Optional[int] = None 
    population: Optional[int] = None 