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
connection.commit()
connection.close()


#Base de Datos No.3
connection = sqlite3.connect('SQLI03.db')


with open('schemaSQLi03.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion, ciudad, pais, tesoro) VALUES (?,?,?,?,?,?,?)",
            (1, 'Juan','Bach','95','turingia','alemania','nada'))

cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion, ciudad, pais, tesoro) VALUES (?,?,?,?,?,?,?)",
            (2, 'Ludwig','Bethoven','98','bonn','alemania', 'nada'))
cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion, ciudad, pais, tesoro) VALUES (?,?,?,?,?,?,?)",
            (3, 'Federico','Chopin','96','varsovia','polonia','nada'))
cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion, ciudad, pais, tesoro) VALUES (?,?,?,?,?,?,?)",
            (4, 'Jorge','Handel','95','halle','alemania','nada'))
cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion, ciudad, pais, tesoro) VALUES (?,?,?,?,?,?,?)",
            (5, 'Wolfgang','Mozart','100','salsburgo','austria','nada'))
cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion, ciudad, pais, tesoro) VALUES (?,?,?,?,?,?,?)",
            (6, 'John','Williams','100','nueva york','eeuu', 'nada'))
cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion, ciudad, pais, tesoro) VALUES (?,?,?,?,?,?,?)",
            (27011756, 'columna 5 - ciudad','columna 6 - pais','columna 7 - tesoro','Esta es','la clave','738c8372fab9160336f3daad7fcc7e2a'))

connection.commit()
connection.close()
