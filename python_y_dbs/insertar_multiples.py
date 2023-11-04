import mysql.connector
conexion1=mysql.connector.connect(host="localhost", user="root",passwd="", database="ejemplo")
cursor1=conexion1.cursor()
sql = "INSERT INTO persona (rut,nombre,apellido,edad) VALUES (%s, %s,%s,%s)"
datos = [ ("6", "kevin","duran",23), ("7", "pedro","molina",63),("8", "Tania","Sobarzo",27)]
cursor1.executemany(sql, datos)
conexion1.commit()
print(cursor1.rowcount, "Se ha insertado")
conexion1.close()
