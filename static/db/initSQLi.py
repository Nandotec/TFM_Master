import sqlite3

connection = sqlite3.connect('SQLI01.db')

# Base de Datos No.1
with open('schemaSQLi.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion) VALUES (?,?,?,?)",
            (1, 'Juan','Bach','95'))

cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion) VALUES (?,?,?,?)",
            (2, 'Ludwig','Bethoven','98'))
cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion) VALUES (?,?,?,?)",
            (3, 'Federico','Chopin','96'))
cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion) VALUES (?,?,?,?)",
            (4, 'Jorge','Handel','95'))
cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion) VALUES (?,?,?,?)",
            (5, 'Wolfgang','Mozart','100'))
cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion) VALUES (?,?,?,?)",
            (6, 'John','Williams','100'))
cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion) VALUES (?,?,?,?)",
            (101092022, 'Esta','es la clave','6e1fcd704528ad8bf6d6bbedb9210096'))

connection.commit()
connection.close()


#Base de datos No.2
connection = sqlite3.connect('SQLI02.db')


with open('schemaSQLi.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion) VALUES (?,?,?,?)",
            (1, 'Juan','Bach','95'))

cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion) VALUES (?,?,?,?)",
            (2, 'Ludwig','Bethoven','98'))
cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion) VALUES (?,?,?,?)",
            (3, 'Federico','Chopin','96'))
cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion) VALUES (?,?,?,?)",
            (4, 'Jorge','Handel','95'))
cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion) VALUES (?,?,?,?)",
            (5, 'Wolfgang','Mozart','100'))
cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion) VALUES (?,?,?,?)",
            (6, 'John','Williams','100'))
cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion) VALUES (?,?,?,?)",
            (108021932, 'Esta','es la clave','7dff51ca8eb990122513f24ffdaa4d9a'))

connection.commit()
connection.close()


#Base de Datos No.3
connection = sqlite3.connect('SQLI03.db')


with open('schemaSQLi.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion) VALUES (?,?,?,?)",
            (1, 'Juan','Bach','95'))

cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion) VALUES (?,?,?,?)",
            (2, 'Ludwig','Bethoven','98'))
cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion) VALUES (?,?,?,?)",
            (3, 'Federico','Chopin','96'))
cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion) VALUES (?,?,?,?)",
            (4, 'Jorge','Handel','95'))
cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion) VALUES (?,?,?,?)",
            (5, 'Wolfgang','Mozart','100'))
cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion) VALUES (?,?,?,?)",
            (6, 'John','Williams','100'))
cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion) VALUES (?,?,?,?)",
            (27011756, 'Esta','es la clave','738c8372fab9160336f3daad7fcc7e2'))

connection.commit()
connection.close()
