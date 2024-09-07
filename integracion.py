import sqlite3

con= sqlite3.connect('data.db')

print ('Conexión exitosa de base de datos')

con.execute('''CREATE TABLE if not EXISTS PERSONA
 (ID INT PRIMARY KEY NOT NULL,
 NOMBRE TEXT NOT NULL,
 EDAD INT NOT NULL,
 DIRECCION CHAR(50));''')
print("¡Tabla creada exitosamente!");
con.close()

con = sqlite3.connect('data.db')
# con.execute('''INSERT INTO PERSONA 
#  (ID,NOMBRE,EDAD,DIRECCION) \
#  VALUES (3,'Pablo',32,'Av. Chaco 123')''');
# con.execute('''INSERT INTO PERSONA
#  (ID,NOMBRE,EDAD,DIRECCION) \
#  VALUES (4, 'Ana', 25, 'Av. Nueva 123')''');
# con.commit()
# print("¡Registros guardados exitosamente!");
# #con.close()

cursor = con.execute('SELECT * FROM persona')
for row in cursor:
    print(row)
    
con.execute('UPDATE PERSONA set DIRECCION = "Calle 3" where ID = 3')
con.commit()
print("Filas actualizadas :", con.total_changes)
cursor = con.execute("SELECT id, nombre, direccion from PERSONA")

print("\nRegistros después de la actualización: ")
cursor = con.execute('SELECT * FROM persona')
for row in cursor:
    print(row)