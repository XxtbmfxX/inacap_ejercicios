import mysql.connector


conexion1=mysql.connector.connect(host="localhost", user="root",passwd="", database="ejemplo")
cursor1=conexion1.cursor()
sql="insert into persona(rut, nombre,apellido,edad) values (%s,%s,%s,%s)"
datos=("3", "raul","santos",23)
cursor1.execute(sql, datos)
datos=("4", "matias","donoso",47)
cursor1.execute(sql, datos)
datos=("5", "maria","gutierrez",23)
cursor1.execute(sql, datos)
conexion1.commit()  		#se utiliza para hacer efectiva la escritura de datos
conexion1.close() 
