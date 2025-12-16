from typing import Annotated
from pydantic import BaseModel, Field


class AllCasesSchema(BaseModel):
    ultima_atualizacao: Annotated[int, Field(ge=0)]

    casos_totais: Annotated[int, Field(ge=0)]
    casos_hoje: Annotated[int, Field(ge=0)]

    obitos_totais: Annotated[int, Field(ge=0)]
    obitos_hoje: Annotated[int, Field(ge=0)]

    recuperados_totais: Annotated[int, Field(ge=0)]
    recuperados_hoje: Annotated[int, Field(ge=0)]

    casos_ativos: Annotated[int, Field(ge=0)]
    casos_criticos: Annotated[int, Field(ge=0)]

    casos_por_milhao_habitantes: Annotated[int, Field(ge=0)]
    obitos_por_milhao_habitantes: Annotated[float, Field(ge=0.0)]

    total_testes: Annotated[int, Field(ge=0)]
    testes_por_milhao_habitantes: Annotated[float, Field(ge=0.0)]

    populacao_total: Annotated[int, Field(ge=0)]

    uma_pessoa_por_caso: Annotated[int, Field(ge=0)]
    uma_pessoa_por_obito: Annotated[int, Field(ge=0)]
    uma_pessoa_por_teste: Annotated[int, Field(ge=0)]

    casos_ativos_por_milhao_habitantes: Annotated[float, Field(ge=0.0)]
    recuperados_por_milhao_habitantes: Annotated[float, Field(ge=0.0)]
    criticos_por_milhao_habitantes: Annotated[float, Field(ge=0.0)]

    numero_paises_afetados: Annotated[int, Field(ge=0)]
