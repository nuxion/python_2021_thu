# Clase 4
# Base de datos
import sqlite3


def create_db(name):
    conn = sqlite3.connect(name)
    c = conn.cursor()
    try:
        c.execute("""CREATE TABLE IF NOT EXISTS Person (
                                            id integer PRIMARY KEY,
                                            firstname text NOT NULL,
                                            lastname text,
                                            age text
                                        ); """)
    except sqlite3.OperationalError as e:
        print(e)

    conn.close()

def get_persons(cursor):
    cursor.execute("""select * from Person;""")
    results = cursor.fetchall()
    for row in results:
        # print(row)
        print(f"Id: {row[0]}, firstname: {row[1]}, lastname: {row[2]}")
    return results


# select
conn = sqlite3.connect("test.db")
c = conn.cursor()
get_persons(c)
# c.execute("insert into Person values(?, ?,?,?)", (4, "maria","garcia", "30"))
conn.commit()

get_persons(c)

