from sqlalchemy import Column, Integer, Float, DateTime, String
from infrastructure.database.models.base import Base


class ProcessedCountries(Base):
    __tablename__ = "processed_countries"

    id = Column(Integer, primary_key=True, autoincrement=True)

    ultima_atualizacao = Column(DateTime, nullable=False)

    pais = Column(String(120), nullable=False)

    casos_totais = Column(Integer, nullable=False)
    casos_hoje = Column(Integer, nullable=False)

    obitos_totais = Column(Integer, nullable=False)
    obitos_hoje = Column(Integer, nullable=False)

    recuperados = Column(Integer, nullable=False)
    recuperados_hoje = Column(Integer, nullable=False)

    casos_ativos = Column(Integer, nullable=False)
    casos_criticos = Column(Integer, nullable=False)

    casos_por_milhao_habitantes = Column(Integer, nullable=False)
    obitos_por_milhao_habitantes = Column(Integer, nullable=False)

    total_testes = Column(Integer, nullable=False)
    testes_por_milhao_habitantes = Column(Integer, nullable=False)

    populacao_total = Column(Integer, nullable=False)

    continente = Column(String(60), nullable=False)

    pessoas_por_caso = Column(Integer, nullable=False)
    pessoas_por_obito = Column(Integer, nullable=False)
    pessoas_por_teste = Column(Integer, nullable=False)

    casos_ativos_por_milhao_habitantes = Column(Float, nullable=False)
    recuperados_por_milhao_habitantes = Column(Float, nullable=False)
    criticos_por_milhao_habitantes = Column(Float, nullable=False)

    Iso2 = Column(String(15), nullable=False)
    Iso3 = Column(String(15), nullable=False)

    Lat = Column(Float, nullable=False)
    Long = Column(Float, nullable=False)
