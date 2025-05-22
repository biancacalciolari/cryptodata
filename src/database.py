import sqlite3

def create_connection(db_file):
    """Cria uma conexão com o banco de dados SQLite"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    """Cria a tabela cryptos no banco de dados"""
    try:
        sql_create_cryptos_table = """
        CREATE TABLE IF NOT EXISTS cryptos (
            id TEXT PRIMARY KEY,
            rank INTEGER,
            name TEXT,
            symbol TEXT,
            priceUsd REAL,
            changePercent24Hr REAL
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_cryptos_table)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def insert_crypto(conn, crypto):
    """Insere um registro de criptomoeda no banco"""
    try:
        sql_insert = """
        INSERT OR REPLACE INTO cryptos (id, rank, name, symbol, priceUsd, changePercent24Hr)
        VALUES (?, ?, ?, ?, ?, ?);
        """
        data = (
            crypto.get("id"),
            int(crypto.get("rank")),
            crypto.get("name"),
            crypto.get("symbol"),
            float(crypto.get("priceUsd")),
            float(crypto.get("changePercent24Hr"))
        )
        cursor = conn.cursor()
        cursor.execute(sql_insert, data)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
