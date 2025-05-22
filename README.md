# Desafio Técnico - CriptoDados 📊

Este projeto foi desenvolvido como parte de um desafio técnico e consiste em consumir dados da API [CoinCap](https://coincap.io/), armazená-los em um banco de dados SQLite, exportá-los para CSV e criar um dashboard analítico com Power BI.

## 🔧 Tecnologias Utilizadas

- Python 3.10+
- Bibliotecas: `requests`, `sqlite3`, `pandas`, `dotenv`
- Power BI Desktop
- Git & GitHub

## 📁 Estrutura do Projeto

```
cryptodata/
│
├── src/
│   ├── api.py               # Consumo da API CoinCap
│   ├── database.py          # Criação do banco e inserção dos dados
│   ├── export_csv.py        # Exportação para CSV
│   ├── main.py              # Execução principal do pipeline
│   └── utils.py             # Funções auxiliares de transformação
│
├── crypto.db                # Banco de dados SQLite gerado
├── cryptos.csv              # Dados exportados em CSV
├── dashboard.pbix           # Dashboard Power BI com gráficos e análises
├── README.md                # Documentação do projeto
└── .gitignore               # Arquivos ignorados pelo Git
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
- O projeto não utiliza autenticação (API CoinCap sem chave obrigatória no endpoint usado).

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Feito com 💙 por [Bianca Calciolari](https://github.com/biancacalciolari)