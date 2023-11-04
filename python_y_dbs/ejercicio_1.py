#ingresar rut, nombre, apellido, edad
#validar
#insertar
#preguntar si continuar
#si -> hacer de nuevo; no -> mostrar 

import sqlite3


def crear_db():
    # Crear una conexión y un cursor
    conexion = sqlite3.connect('ejemplo.db')
    cursor = conexion.cursor()

    # Crear la tabla persona si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS persona (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rut TEXT,
            nombre TEXT,
            apellido TEXT,
            edad INTEGER
        )
    ''')

    # Insertar datos de ejemplo
    datos_ejemplo = [
        ('12345678-9', 'Juan', 'Perez', 30),
        ('98765432-1', 'Maria', 'Lopez', 25),
        ('55555555-5', 'Pedro', 'Gomez', 35)
    ]

    cursor.executemany('INSERT INTO persona (rut, nombre, apellido, edad) VALUES (?, ?, ?, ?)', datos_ejemplo)

    # Commit y cerrar conexión
    conexion.commit()
    conexion.close()


def verificar_en_db(rut):
    conexion1 = sqlite3.connect('ejemplo.db')  # Nombre de la base de datos SQLite
    cursor1 = conexion1.cursor()
    cursor1.execute(f"SELECT rut FROM persona WHERE rut = ?", (rut,))
    fila = cursor1.fetchone()
    if fila:
        print(fila)
        return True
    else:
        return False
    conexion1.close()

def validar_rut(rut):
    rut = rut.replace(".", "").replace("-", "").upper()
    if len(rut) < 8 or not rut[:-1].isdigit() or not rut[-1] in "0123456789K":
        return False

    reversed_digits = list(map(int, reversed(rut[:-1])))
    factors = [2, 3, 4, 5, 6, 7, 2, 3]

    total = sum(digit * factor for digit, factor in zip(reversed_digits, factors))
    remainder = total % 11

    valid_digit = 11 - remainder if remainder != 0 else 0
    expected_digit = int(rut[-1]) if rut[-1].isdigit() else 10

    return valid_digit == expected_digit

def formatear_rut(rut):
    rut = rut.replace(".", "").replace("-", "").upper()
    return f"{rut[:-1]}-{rut[-1]}"

def preguntar_rut():
    while True:
        rut = input("Ingresa tu RUT (sin puntos ni guión): ")
        
        if not validar_rut(rut):
            print("El RUT ingresado no es válido. Por favor, inténtalo nuevamente.")
            continue
        
        rut = formatear_rut(rut)

        if verificar_en_db(rut):
            print("El RUT ya existe en la base de datos. Por favor, ingresa otro.")
            continue

        return rut

        break

#Evitar repetir código en nombre y apellido
def validar_input(mensaje):
    while True:
        try:
            entrada = input(mensaje + " (^人^) ")
            return entrada

        except:
            print(f"Tiene que ser una entrada válida (ง •_•)ง ")

def validar_nombre():
    return validar_input("Deme su nombre porfis")

def validar_apellido():
    return validar_input("Deme su apellido porfis")

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
    conexion1 = sqlite3.connect('ejemplo.db')  # Nombre de la base de datos SQLite
    cursor1 = conexion1.cursor()
    
    sql = "INSERT INTO persona(rut, nombre, apellido, edad) VALUES (?, ?, ?, ?)"
    cursor1.execute(sql, datos)
    
    conexion1.commit()
    conexion1.close() 

def mostrar_datos():
    conexion1 = sqlite3.connect('ejemplo.db')  # Nombre de la base de datos SQLite
    cursor1 = conexion1.cursor()
    cursor1.execute("SELECT * FROM persona")
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

def main():

    crear_db()

    print("\n =====  \(@^0^@)/ Programa para ingresar personas \(@^0^@)/  ===== \n")
    while True:
        rut = preguntar_rut()
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