from sqlalchemy import Column, BigInteger, Float, DateTime, Integer
from infrastructure.database.models.base import Base


class ProcessedAllCases(Base):
    __tablename__ = "processed_all_cases"

    id = Column(Integer, primary_key=True, autoincrement=True)

    ultima_atualizacao = Column(DateTime, nullable=False)

    casos_totais = Column(BigInteger, nullable=False)
    casos_hoje = Column(BigInteger, nullable=False)

    obitos_totais = Column(BigInteger, nullable=False)
    obitos_hoje = Column(BigInteger, nullable=False)

    recuperados_totais = Column(BigInteger, nullable=False)
    recuperados_hoje = Column(BigInteger, nullable=False)

    casos_ativos = Column(BigInteger, nullable=False)
    casos_criticos = Column(BigInteger, nullable=False)

    casos_por_milhao_habitantes = Column(BigInteger, nullable=False)
    obitos_por_milhao_habitantes = Column(Float, nullable=False)

    total_testes = Column(BigInteger, nullable=False)
    testes_por_milhao_habitantes = Column(Float, nullable=False)

    populacao_total = Column(BigInteger, nullable=False)

    uma_pessoa_por_caso = Column(BigInteger, nullable=False)
    uma_pessoa_por_obito = Column(BigInteger, nullable=False)
    uma_pessoa_por_teste = Column(BigInteger, nullable=False)

    casos_ativos_por_milhao_habitantes = Column(Float, nullable=False)
    recuperados_por_milhao_habitantes = Column(Float, nullable=False)
    criticos_por_milhao_habitantes = Column(Float, nullable=False)

    numero_paises_afetados = Column(BigInteger, nullable=False)
