# Covid ETL Pipeline

Projeto pessoal de **ETL em Python** para coleta, transformação e futura persistência de dados relacionados à Covid-19, seguindo **boas práticas de engenharia de dados**, **arquitetura em camadas** e **separação por domínio**.

> ⚠️ **Status atual**: a camada de banco de dados (conexão PostgreSQL e models SQLAlchemy) **ainda não está implementada**, mas **todas as entidades e estruturas já estão preparadas** para inclusão futura.

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

  * Persistência em PostgreSQL
  * Orquestração futura (Airflow, Prefect, etc.)
  * Exposição via API

---

## 🧱 Arquitetura Geral

O projeto está organizado dentro do diretório `src/` e segue uma separação clara de responsabilidades:

```
src/
├── app/              # Ponto de entrada da aplicação
├── domain/           # Regras de negócio, contratos e DTOs
├── pipeline/         # Implementação do ETL (extract + transform)
├── infrastructure/  # Infraestrutura (DB, schemas, segurança)
├── settings/         # Configurações globais e logging
```

---

## 📁 Estrutura de Diretórios (Detalhada)

### `app/`

Responsável por iniciar a aplicação.

* `main.py`: ponto inicial de execução

---

### `domain/`

Camada central do projeto. **Não depende de infraestrutura**.

#### `domain/dtos/`

DTOs (Data Transfer Objects) que representam os dados tratados no pipeline:

* `all_cases.py`
* `continents.py`
* `countries.py`

#### `domain/interfaces/`

Contratos e classes base:

* `extract.py`: interface de extração
* `transform_base.py`: classe base para transformações
* `transform_pipeline.py`: contrato do pipeline de transformação

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

* `extract.py`: lógica de extração de dados
* `transform_pipeline.py`: orquestra as transformações

#### `pipeline/transformers/`

Transformações específicas por entidade:

* `all_cases.py`
* `continents.py`
* `countries.py`

Cada transformer segue contratos definidos no domínio.

---

### `infrastructure/`

Camada responsável por detalhes técnicos externos.

#### `infrastructure/database/`

Preparada para persistência com PostgreSQL + SQLAlchemy.

* `connections/postgre.py`: **(ainda não implementado)** conexão com o banco
* `schemas/`: schemas das entidades

  * `all_cases.py`
  * `continents.py`
* `models/`: **reservado para models SQLAlchemy**
* `security/credential_postgres.py`: credenciais do banco

> ⚠️ Models e conexão ainda não foram implementados, mas a estrutura já está pronta.

---

### `settings/`

Configurações globais do projeto:

* `constants.py`: constantes globais
* `loggin.py` / `log_fire.py`: configuração de logs

---

## ▶️ Como Executar o Projeto

### 1️⃣ Ative o ambiente virtual

O projeto utiliza `.venv`.

### 2️⃣ Execução via Makefile (Recomendado)

O projeto **não é executado a partir da raiz**, mas sim utilizando o módulo `src.pipeline`.

No `Makefile`:

```
ifeq ($(OS),Windows_NT)
    PYTHON=python
    ACTIVATE=call .venv\Scripts\activate
else
    PYTHON=python3
    ACTIVATE=. .venv/bin/activate
endif

run:
	$(ACTIVATE) && $(PYTHON) -m src.pipeline
```

Execute:

```
make run
```

---

## 🧪 Estado Atual do Pipeline

* ✅ Extração implementada
* ✅ Transformações por entidade
* ✅ Validações e DTOs
* ✅ Logging estruturado
* ⏳ Persistência no banco (em desenvolvimento)
* ⏳ Models SQLAlchemy (em desenvolvimento)

---

## 🛣️ Próximos Passos Planejados

* Implementar conexão PostgreSQL
* Criar models SQLAlchemy
* Implementar camada de load
* Adicionar testes automatizados
* Criar versionamento de schemas
* Evoluir para orquestração (Airflow / Prefect)

---

## 📌 Observações Importantes

* Projeto **pessoal**, focado em aprendizado profundo
* Estrutura pensada para **crescer sem refatorações grandes**
* Todas as decisões arquiteturais priorizam:

  * Clareza
  * Manutenibilidade
  * Escalabilidade

---

## 👤 Autor

**André Luiz**
Projeto pessoal de engenharia de dados com Python 🚀
