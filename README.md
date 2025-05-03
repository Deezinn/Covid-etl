# 🦠 COVID-19 ETL por País

Este projeto realiza um processo de **ETL (Extract, Transform, Load)** com dados da COVID-19 relacionados aos países. Os dados são extraídos de uma API, transformados e carregados para uso analítico.

## 📁 Estrutura do Projeto

ETL_COVID/
│
├── src/
│ ├── extract/
│ │ └── httpData.py
│ │
│ ├── load/
│ │ └── loadData.py ← Arquivo principal para rodar o ETL
│ │
│ ├── transform/
│ │ ├── transformCovid.py
│ │ └── urlApis.json ← Contém as URLs de onde os dados são extraídos
│
├── requirements.txt


## ▶️ Como Executar

1. **Clone o repositório**
   ```bash
   git clone https://github.com/Deezinn/covid-etl.git
   cd covid-etl

    Crie um ambiente virtual (opcional, mas recomendado)

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

Instale as dependências

pip install -r requirements.txt

Execute o ETL

python src/load/loadData.py
