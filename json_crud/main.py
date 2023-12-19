from utils import *
from json_functions import listar_alumnos

def main():
    while True:    
        res = preguntar_que_hacer()

        match res:
            case "1":
                ingresar_alumno()
            
            case "2":
                listar_alumnos()
            
            case "3":
                quit()
            
            case _:
                print("🥸")
            

if __name__ == "__main__":
    main()