import sqlite3

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
