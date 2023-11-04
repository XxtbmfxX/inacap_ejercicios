#ingresar rut, nombre, apellido, edad
#validar
#insertar
#preguntar si continuar
#si -> hacer de nuevo; no -> mostrar 

import mysql.connector

def verificar_en_db(rut):
    conexion1=mysql.connector.connect(host="localhost", user="root",passwd="", database="ejemplo")
    cursor1=conexion1.cursor()
    cursor1.execute(f"select rut from persona where rut = {rut}")
    for fila in cursor1:
        print(fila)
        if fila:
            return True
        else:
            False
    conexion1.close()

def validar_rut():
    while True:
        try:
            rut = int(input("Deme su rut porfis (●'◡'●) "))
            if verificar_en_db(rut):
                raise ValueError
            else:
                return rut
        except:
            print("Rut Invalido o existente ╰（‵□′）╯")

def validar_nombre():
    while True:
        try:
            nombre = input("Deme su nombre porfis (^人^) ")
            return nombre

        except:
            print("Tiene que ser un nombre valido (ง •_•)ง ")

def validar_apellido():
   while True:
        try:
            apellido = input("Deme su apellido porfis (^人^) ")
            return apellido

        except:
            print("Tiene que ser un apellido valido (ง •_•)ง ")

def validar_edad():
    while True:
        try:
            edad = int(input("Deme su edad porfis (○｀ 3′○) "))
            if edad < 0 or edad > 100:
                raise ValueError
            else:
                return edad
        except:
            print("Edad invalidad (╬▔皿▔)╯ ")

def insertar_en_persona(datos: tuple):    
    conexion1=mysql.connector.connect(host="localhost", user="root",passwd="", database="ejemplo")
    cursor1=conexion1.cursor()
    
    sql="insert into persona(rut, nombre, apellido, edad) values (%s,%s,%s,%s)"
    cursor1.execute(sql, datos)
    
    conexion1.commit()
    conexion1.close() 

def mostrar_datos():
    conexion1=mysql.connector.connect(host="localhost", user="root",passwd="", database="ejemplo")
    cursor1=conexion1.cursor()
    cursor1.execute("select * from persona")
    for fila in cursor1:
        print(fila)
    conexion1.close() 

def preguntar_continuar():
    while True:
        try:
            continuar = input("Desea continuar? si/no ").lower()
            if continuar not in ["si", "no"]:
                raise ValueError
            elif continuar == "si":
                return True
            else:
                return False
        except:
            print("SI O NO ┗|｀O′|┛")

def preguntar_que_hacer():
    print("""
    1. Desea mostra los datos
    2. Desea agregar una persona
    3. Hacer algo random
    """)
    while True:
        try:
            opcion = input("Desea mostrar los datos ").lower()
            if opcion not in ["si", "no"]:
                raise ValueError
            elif opcion == "si":
                return True
            else:
                return False
        except:
            print("SI O NO ┗|｀O′|┛")

def main():



    while True:
        rut = validar_rut()
        nombre = validar_nombre()
        apellido = validar_apellido()
        edad = validar_edad()

        datos = (rut, nombre, apellido, edad)

        insertar_en_persona(datos)

        if preguntar_continuar():
            continue
        else:
            mostrar_datos()
            quit()




if __name__ == "__main__":
    main()