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
            (101092022, 'Esta','es la clave','d5233f38eed5ca5a5fe20a3da852a3cb'))

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
            (27011756, 'columna 5 - ciudad','columna 6 - pais','columna 7 - tesoro','Esta es','la clave','f7e9050c92a851b0016442ab604b0488'))

connection.commit()
connection.close()
