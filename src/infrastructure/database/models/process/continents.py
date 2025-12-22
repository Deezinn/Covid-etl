from sqlalchemy import Column, Integer, Float, DateTime, String, JSON, BigInteger
from infrastructure.database.models.base import Base


class ProcessedContinents(Base):
    __tablename__ = "processed_continents"

    id = Column(Integer, primary_key=True, autoincrement=True)

    ultima_atualizacao = Column(DateTime, nullable=False)

    casos_totais = Column(BigInteger, nullable=False)
    casos_hoje = Column(BigInteger, nullable=False)

    obitos_totais = Column(BigInteger, nullable=False)
    obitos_hoje = Column(BigInteger, nullable=False)

    recuperados = Column(BigInteger, nullable=False)
    recuperados_hoje = Column(BigInteger, nullable=False)

    casos_ativos = Column(BigInteger, nullable=False)
    casos_criticos = Column(BigInteger, nullable=False)

    casos_por_milhao_habitantes = Column(Float, nullable=False)
    obitos_por_milhao_habitantes = Column(Float, nullable=False)

    total_testes = Column(BigInteger, nullable=False)
    testes_por_milhao_habitantes = Column(Float, nullable=False)

    populacao_total = Column(BigInteger, nullable=False)

    continente = Column(String(60), nullable=False)

    casos_ativos_por_milhao_habitantes = Column(Float, nullable=False)
    recuperados_por_milhao_habitantes = Column(Float, nullable=False)
    criticos_por_milhao_habitantes = Column(Float, nullable=False)

    # lista final já tratada (derivada do RAW)
    paises = Column(JSON, nullable=False)

    continente_lat = Column(Float, nullable=False)
    continente_long = Column(Float, nullable=False)
