from typing import Annotated, List
from pydantic import BaseModel, Field
from datetime import datetime

class ContinentsSchema(BaseModel):
    ultima_atualizacao: datetime
    
    casos_totais: Annotated[int, Field(ge=0)]
    casos_hoje: Annotated[int, Field(ge=0)]

    obitos_totais: Annotated[int, Field(ge=0)]
    obitos_hoje: Annotated[int, Field(ge=0)]

    recuperados: Annotated[int, Field(ge=0)]
    recuperados_hoje: Annotated[int, Field(ge=0)]

    casos_ativos: Annotated[int, Field(ge=0)]
    casos_criticos: Annotated[int, Field(ge=0)]

    casos_por_milhao_habitantes: Annotated[float, Field(ge=0)]
    obitos_por_milhao_habitantes: Annotated[float, Field(ge=0.0)]

    total_testes: Annotated[int, Field(ge=0)]
    testes_por_milhao_habitantes: Annotated[float, Field(ge=0.0)]

    populacao_total: Annotated[int, Field(ge=0)]

    continente: Annotated[str, Field(max_length=60)]
    
    casos_ativos_por_milhao_habitantes: Annotated[float, Field(ge=0.0)]
    recuperados_por_milhao_habitantes: Annotated[float, Field(ge=0.0)]
    criticos_por_milhao_habitantes: Annotated[float, Field(ge=0.0)]
    
    paises: List[str]
    
    continente_lat: float
    continente_long: float