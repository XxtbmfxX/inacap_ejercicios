def ingresar_nombre() -> str:
    while True:
        try:
            nombre = input("Deme su nombre porfis (^人^) ")
            if not nombre.isalpha():
                raise ValueError("Tiene que ser un nombre valido (ง •_•)ง ")
            if len(nombre) < 3 or len(nombre) > 12:
                raise ValueError("El nombre debe tener entre 3 y 12 caracteres (╯°□°）╯︵ ┻━┻")
            return nombre
        except ValueError :
            print(ValueError)

def ingresar_rut() -> str:
    while True:
        try:
            rut = input("Deme su rut porfis (^人^) \n (sin puntos, con guión y con dígito verificador) ").lower()
            
            if len(rut) < 9 or len(rut) > 10 :
                raise ValueError("Tiene que ser un rut valido (•_•) ")
            
            if not rut[:-2].isdigit():
                raise ValueError("Tiene que ser un rut valido (•_•) ")
                
            if rut[-1] not in "0123456789k":
                raise ValueError("Tiene que ser un rut valido (•_•) ")
               
                
            if rut[-2] != "-":
                raise ValueError("Tiene que ser un rut valido (•_•) ")

             
            return rut
            
        except ValueError :
            print(ValueError)

def ingresar_notas():
    notas = []
    
    for i in range(3):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {i + 1} ( •̀ ω •́ )✧ "))
                
                if 1.0 <= nota <= 7.0:
                    notas.append(nota)
                    break
                else:
                    print("Error: La nota debe estar en el rango de 1.0 a 7.0.")
            except ValueError:
                print("Error: Por favor, ingrese un valor numérico válido.")
    
    return notas

def calcular_promedio(notas):
    if not notas:
        return None  # Devuelve None si la lista de notas está vacía
    
    suma_notas = sum(notas)
    cantidad_notas = len(notas)
    promedio = suma_notas / cantidad_notas
    
    return promedio

def verificar_aprobado(notas, promedio):
    
    if promedio is not None:
        if promedio >= 4.0 and all(nota >= 4.0 for nota in notas):
            return "Aprobado"
        elif promedio >= 4.0:
            return "Rendir Examen"
        else:
            return "Reprobado"
    else:
        return "No se pueden verificar notas sin datos."


#funciones del menú

def preguntar_que_hacer():
    while True:
        try:
            user = input("""
                1. para Ingresar un alumno
                2. Para listar alumnos
                3. Para salir
            """)
                    
            if user not in ["1","2","3"]:
                raise ValueError("Tiene que elegir una de las opciones >.<")         

            return user   
    
        except ValueError:
            print(ValueError)

def ingresar_alumno():
    rut = ingresar_rut()
    nombre = ingresar_nombre()
    notas = ingresar_notas()  
    promedio = calcular_promedio(notas)
    aprobado = verificar_aprobado(notas, promedio)
    
    [rut] = (nombre, notas, promedio, aprobado)

    
      

def lsitar_alumno():
    pass