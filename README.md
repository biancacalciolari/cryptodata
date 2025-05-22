# 📊 Desafio Técnico - CryptoData

Este projeto faz parte de um desafio técnico que tem como objetivo a **coleta de dados de criptomoedas**, o **armazenamento em banco de dados relacional**, a **exportação para CSV** e a **criação de um dashboard interativo em Power BI**.

---

## 🚀 Objetivo

Consumir dados da [API CoinCap](https://docs.coincap.io/), armazenar os dados em uma base SQLite, transformá-los, exportá-los para um arquivo `.csv`, e então criar dashboards de visualização de KPIs e análises com **Power BI**.

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- SQLite
- Pandas
- Requests
- Power BI

## 🗂️ Estrutura do Projeto

cryptodata/

│

├── data/

│   └── cryptos.csv          # Arquivo CSV com os dados processados

│

├── src/

│   ├── main.py              # Script principal: coleta, trata e salva os dados

│   ├── api.py               # Função para consumir a API da CoinCap

│   ├── database.py          # Funções de conexão e manipulação do banco de dados

│   └── requirements.txt     # Bibliotecas utilizadas no projeto

│

├── crypto.db                # Banco de dados gerado com as informações

│

├── dashboard.pbix           # Dashboard Power BI com gráficos e análises

│

└── README.md                # Este arquivo
