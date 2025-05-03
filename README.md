# 🦠 COVID-19 ETL por País

Este projeto implementa um processo de **ETL (Extract, Transform, Load)** para dados da COVID-19 em nível de país. Através da extração de dados de APIs públicas, sua transformação e posterior carregamento, o projeto visa fornecer uma base de dados estruturada para análises, visualizações e relatórios relacionados à pandemia.

---

## 📁 Estrutura do Projeto

```text
ETL_COVID/
│
├── src/
│   ├── extract/
│   │   └── httpData.py        # Responsável por extrair os dados das APIs.
│   │
│   ├── load/
│   │   └── loadData.py        # Executa o pipeline ETL completo.
│   │
│   ├── transform/
│   │   ├── transformCovid.py  # Realiza a limpeza e transformação dos dados.
│   │   └── urlApis.json       # Arquivo contendo as URLs das APIs com os dados da COVID.
│
├── requirements.txt           # Lista de dependências do projeto.

▶️ Como Executar

Siga os passos abaixo para executar o pipeline ETL:

    Clone o repositório:
    Bash

git clone [https://github.com/Deezinn/covid-etl.git](https://github.com/Deezinn/covid-etl.git)
cd covid-etl

(Opcional) Crie um ambiente virtual (recomendado):
Bash

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

Instale as dependências:
Bash

pip install -r requirements.txt

Execute o pipeline ETL:
Bash

    python src/load/loadData.py

🌐 Fonte de Dados

As URLs das APIs utilizadas para extrair os dados estão definidas no arquivo:

src/transform/urlApis.json

Este projeto se baseia em APIs públicas e confiáveis, como:

    Our World in Data
    COVID-19 API

🎯 Objetivo

    Automatizar a coleta de dados da pandemia por país.
    Estruturar os dados para facilitar análises subsequentes.
    Servir como base para a criação de dashboards e relatórios informativos.
