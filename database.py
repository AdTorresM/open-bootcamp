import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute("""
            CREATE TABLE if not exists alumno (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL
            );
""")


def crear(nombre, apellido):
    query = f"INSERT INTO alumno(nombre, apellido) VALUES(?, ?)"
    cursor.execute(query, (nombre, apellido))
    conn.commit()


crear('Diego', 'Torres')
crear('Adrian', 'Torres')
crear('Daniela', 'Betanzos')
crear('Carmen', 'Montes de Oca')
crear('Alejandro', 'Torres')
crear('Bernardo', 'Corona')
crear('Rodolfo', 'Orea')
crear('Gabriel', 'Valdez')

query = 'SELECT * FROM alumno'
data2 = cursor.execute(query)
for a in data2:
    print(a)

cursor.close()
conn.close()