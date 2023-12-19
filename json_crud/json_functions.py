import json


def cargar_datos_desde_json():
    nombre_archivo="prueba4.json"
    try:
        with open(nombre_archivo, 'r') as archivo:
            datos = json.load(archivo)
        return datos
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe. >.< (vamos a crear uno) ")
        return None

def listar_alumnos():
    data = cargar_datos_desde_json()
    
    if data:
        for alumno in data["alumnos"]:
            print(alumno["rut"]) 
    else:
        print("No hay datos (´･ω･`)?...   ")

listar_alumnos()