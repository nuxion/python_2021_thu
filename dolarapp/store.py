import sqlite3

_TABLE = """
CREATE TABLE IF NOT EXISTS "dolar" (
	"blue"	REAL NOT NULL,
	"oficial"	REAL NOT NULL,
	"timestamp"	NUMERIC
);"""

_DBNAME = "test.db"

def create_db(dbname, table):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    try:
        c.execute(table)
    except sqlite3.OperationalError as e:
        print(e)

    conn.close()

def insert_cotizacion(dbname, table, values):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c = c.execute(f'INSERT into {table} values(?, ?, ?)', values)
    conn.commit()

if __name__=="__main__":
    create_db(_DBNAME, _TABLE)
    insert_cotizacion(_DBNAME, "dolar", (46.5, 56.5, 0))
