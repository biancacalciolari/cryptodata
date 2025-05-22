# Desafio Técnico - CriptoDados 📊

Este projeto foi desenvolvido como parte de um desafio técnico e consiste em consumir dados da API [CoinCap](https://coincap.io/), armazená-los em um banco de dados SQLite, exportá-los para CSV e criar um dashboard analítico com Power BI.

## 🔧 Tecnologias Utilizadas

- Python 3.x
- SQLite
- Pandas
- Requests
- Power BI
- VSCode / Anaconda

## 📁 Estrutura do Projeto

```
cryptodata/
│
├── data/
│ └── cryptos.csv # Arquivo CSV com os dados processados
│
├── src/
│ ├── main.py # Script principal: coleta, trata e salva os dados
│ ├── api.py # Função para consumir a API da CoinCap
│ ├── database.py # Funções de conexão e manipulação do banco de dados
│ └── requirements.txt # Bibliotecas utilizadas no projeto
│
├── crypto.db # Banco de dados gerado com as informações
│
├── dashboard.pbix # Dashboard Power BI com gráficos e análises
│
└── README.md # Este arquivo

```

## 🚀 Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/biancacalciolari/cryptodata.git
cd cryptodata
```

2. Crie um ambiente virtual e instale as dependências:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

3. Execute o pipeline para gerar banco de dados e CSV:

```bash
cd src
python main.py
```

4. Abra o `dashboard.pbix` com o Power BI Desktop para visualizar os dados.

## 📊 Dashboard Power BI

O dashboard contém:

- Tabela de detalhes das criptomoedas
- Gráfico de barras com os preços
- Gráfico de variação percentual 24h
- Filtros interativos por nome e símbolo

## 📌 Observações

- O campo `changePercent24Hr` é transformado em percentual (ex: 1.15 → 115%).

---

Feito com 💙 por [Bianca Calciolari](https://github.com/biancacalciolari)
