from typing import Annotated, List
from pydantic import BaseModel, Field
from datetime import datetime

class CountriesSchema(BaseModel):
    ultima_atualizacao: datetime
    pais: str
    casos_totais: Annotated[int, Field(ge=0)]
    casos_hoje: Annotated[int, Field(ge=0)]
    obitos_totais: Annotated[int, Field(ge=0)]
    obitos_hoje: Annotated[int, Field(ge=0)]
    recuperados: Annotated[int, Field(ge=0)]
    recuperados_hoje: Annotated[int, Field(ge=0)]
    casos_ativos: Annotated[int, Field(ge=0)]
    casos_criticos: Annotated[int, Field(ge=0)]
    casos_por_milhao_habitantes: Annotated[int, Field(ge=0)]
    obitos_por_milhao_habitantes: Annotated[int, Field(ge=0)]
    total_testes: Annotated[int, Field(ge=0)]
    testes_por_milhao_habitantes: Annotated[int, Field(ge=0)]
    populacao_total: Annotated[int, Field(ge=0)]
    continente: str
    pessoas_por_caso: Annotated[int, Field(ge=0)]
    pessoas_por_obito: Annotated[int, Field(ge=0)]
    pessoas_por_teste: Annotated[int, Field(ge=0)]
    casos_ativos_por_milhao_habitantes: Annotated[float, Field(ge=0.0)]
    recuperados_por_milhao_habitantes: Annotated[float, Field(ge=0.0)]
    criticos_por_milhao_habitantes: Annotated[float, Field(ge=0.0)]
    Iso2: str
    Iso3: str
    Lat: float
    Long: float