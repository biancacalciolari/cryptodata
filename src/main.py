from api import get_cryptos
from database import create_connection, create_table, insert_crypto
import pandas as pd
import sqlite3

def main():
    print("Buscando dados de criptomoedas...")
    cryptos = get_cryptos(limit=10)

    conn = create_connection("../crypto.db")
    create_table(conn)

    for crypto in cryptos:
        insert_crypto(conn, crypto)

    print("Exportando dados formatados para CSV...")
    df = pd.read_sql_query("SELECT * FROM cryptos", conn)

    # Transformação: formatar a coluna de variação percentual
    df["changePercent24Hr"] = pd.to_numeric(df["changePercent24Hr"], errors="coerce")
    df["changePercent24HrFormatted"] = df["changePercent24Hr"].mul(100).round(0).astype(int).astype(str) + "%"

    df.to_csv("../cryptos_formatado.csv", index=False)
    print("Arquivo 'cryptos_formatado.csv' criado com sucesso.")

if __name__ == "__main__":
    main()
