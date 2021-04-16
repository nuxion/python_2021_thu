# clase 4
# base de datos
import pymysql.cursors

conn = pymysql.connect(
    host="localhost", user="root", password="secret",
    database="educacionit")
    # otra forma en que se  pueda configurar una conexion a una base de datos
    # es pasandole un urlstring:
    # pymysql+Mysql://root:secret@localhost:3306/educacionit"

def insert_person(cursor, firstname, lastname):
    cursor.execute("INSERT into person (`firstname`,`lastname`) values (%s,%s)", (firstname, lastname))

cursor = conn.cursor()
insert_person(cursor, "Maria", "Perez")
conn.commit()

cursor.execute("Select * from person;")
rows = cursor.fetchall()
for r in rows:
    print(r)
