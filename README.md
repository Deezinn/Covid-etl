# 🦠 COVID-19 ETL por País

Este projeto realiza um processo de **ETL (Extract, Transform, Load)** com dados da COVID-19 relacionados aos países. Os dados são extraídos de APIs públicas, transformados e carregados para posterior análise, sendo úteis para visualizações, relatórios ou estudos.

---

## 📁 Estrutura do Projeto

```text
ETL_COVID/
│
├── src/
│   ├── extract/
│   │   └── httpData.py
│   │       # Responsável por extrair os dados das APIs.
│   │
│   ├── load/
│   │   └── loadData.py
│   │       # Executa o pipeline ETL completo.
│   │
│   ├── transform/
│   │   ├── transformCovid.py
│   │   │   # Realiza a limpeza e transformação dos dados.
│   │   └── urlApis.json
│   │       # Arquivo contendo as URLs das APIs com os dados da COVID.
│
├── requirements.txt
│   # Lista de dependências do projeto.

▶️ Como Executar
1. Clone o repositório

git clone https://github.com/Deezinn/covid-etl.git
cd covid-etl

2. (Opcional) Crie um ambiente virtual

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3. Instale as dependências

pip install -r requirements.txt

4. Execute o pipeline ETL

python src/load/loadData.py

🌐 Fonte de Dados

As URLs das APIs estão definidas em:

src/transform/urlApis.json

As APIs devem ser públicas e confiáveis, como:

    Our World in Data

    COVID-19 API

🎯 Objetivo

    Automatizar a coleta de dados da pandemia por país.

    Estruturar os dados para facilitar análises.

    Servir como base para dashboards e relatórios.
