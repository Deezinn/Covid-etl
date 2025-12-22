# Covid ETL Pipeline

Projeto pessoal de **ETL em Python** para coleta, transformação e **persistência de dados** relacionados à Covid-19, seguindo **boas práticas de engenharia de dados**, **arquitetura em camadas** e **separação por domínio**.

> ✅ **Status atual**: o pipeline ETL está **totalmente funcional**, incluindo **extração, transformação e carga (load)**. O projeto suporta **SQLite local automaticamente** e **PostgreSQL via `.env`**.

---

## 🎯 Objetivo do Projeto

* Estruturar um **pipeline de dados robusto** para dados de Covid-19
* Aplicar conceitos de:

  * ETL (Extract, Transform, Load)
  * Arquitetura limpa
  * Domain-driven design (DDD simplificado)
  * Interfaces e contratos
  * Escalabilidade e manutenção
* Servir como **base evolutiva** para:

  * Persistência relacional (SQLite / PostgreSQL)
  * Orquestração futura (Airflow, Prefect, etc.)
  * Exposição via API

---

## 🧱 Arquitetura Geral

O projeto está organizado dentro do diretório `src/` e segue uma separação clara de responsabilidades:

```
src/
├── app/              # Ponto de entrada da aplicação
├── domain/           # Regras de negócio, contratos e DTOs
├── pipeline/         # Implementação do ETL (extract, transform, load)
├── infrastructure/  # Infraestrutura (DB, models, schemas, conexões)
├── settings/         # Configurações globais e logging
```

---

## 📁 Estrutura de Diretórios (Detalhada)

### `app/`

Responsável por iniciar a aplicação.

* `main.py`: ponto inicial de execução do pipeline

---

### `domain/`

Camada central do projeto. **Não depende de infraestrutura**.

#### `domain/dtos/`

DTOs (Data Transfer Objects) definidos com **`@dataclass`**, representando dados já tratados:

* `all_cases.py`
* `continents.py`
* `countries.py`

#### `domain/interfaces/`

Contratos e abstrações do domínio:

* `extract.py`: contrato de extração
* `transform_base.py`: classe base para transformações
* `transform_pipeline.py`: contrato do pipeline de transformação
* `load.py`: contrato da camada de carga

#### `domain/exceptions/`

Exceções customizadas do domínio:

* `pipeline.py`
* `orchestrator.py`
* `transform.py`

#### `domain/utils/`

Funções utilitárias reutilizáveis:

* `clean_list.py`

---

### `pipeline/`

Implementação prática do ETL.

* `extract.py`: extração dos dados
* `transform_pipeline.py`: orquestra transformações
* `load.py`: executa a carga dos dados

#### `pipeline/transformers/`

Transformações específicas por entidade, utilizando **Pandas**:

* `all_cases.py`
* `continents.py`
* `countries.py`

Cada transformer segue contratos definidos no domínio.

---

### `infrastructure/`

Camada responsável por detalhes técnicos externos.

#### `infrastructure/database/`

Persistência de dados com **SQLAlchemy**.

##### `connections/`

* `factory.py`: factory de conexões
* `postgre.py`: conexão PostgreSQL
* `sqlite.py`: conexão SQLite local
* `loader.py`: executor de carga

> 🔁 **Comportamento automático**:
>
> * Se **não existir `.env`**, o projeto cria automaticamente um banco **`covid.db` (SQLite)**
> * Se **existir `.env`**, a carga é feita no **PostgreSQL**

##### `models/`

Models SQLAlchemy:

* `base.py`: base declarativa
* `raw/`: dados brutos
* `process/`: dados processados

##### `schemas/`

Schemas definidos com **Pydantic**, usados para validação:

* `all_cases.py`
* `continents.py`
* `countries.py`

##### `security/`

* `credential_postgres.py`: leitura segura das credenciais

---

### `settings/`

Configurações globais do projeto:

* `constants.py`: constantes globais
* `loggin.py` / `log_fire.py`: logging estruturado

---

## ▶️ Como Executar o Projeto

### 1️⃣ Ative o ambiente virtual

O projeto utiliza `.venv`.

### 2️⃣ Execução

Execute o pipeline a partir do módulo principal:

```
python3 -m app.main
```

---

## 🧪 Estado Atual do Pipeline

* ✅ Extração implementada
* ✅ Transformações por entidade (Pandas)
* ✅ DTOs com `dataclass`
* ✅ Validações com Pydantic
* ✅ Carga funcional (SQLite / PostgreSQL)
* ✅ Models com SQLAlchemy
* ✅ Logging estruturado

---

## 🛣️ Próximos Passos Planejados

* Adicionar testes automatizados
* Criar versionamento de schemas
* Melhorar observabilidade
* Evoluir para orquestração (Airflow / Prefect)
* Expor dados via API

---

## 📌 Observações Importantes

* Projeto **pessoal**, focado em aprendizado profundo
* Estrutura pensada para **crescer sem refatorações grandes**
* Arquitetura baseada em **contratos e separação de responsabilidades**

---

## 👤 Autor

**André Luiz**
Projeto pessoal de engenharia de dados com Python 🚀
