import sqlite3
con = sqlite3.connect('totorial.db')
cur = con.cursor()

cur.execute('CREATE TABLE movie(titulo, año, puntaje')

res = cur.execute('SELECT name FROM sqlite_master')
res.fetchone()
('pelicula',)