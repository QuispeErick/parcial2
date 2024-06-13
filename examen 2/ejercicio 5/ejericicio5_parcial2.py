import sqlite3


# Función para inicializar la base de datos y cargar datos de ejemplo
def inicializar_base_datos(nombre_bd):
    conn = sqlite3.connect(nombre_bd)
    cursor = conn.cursor()

    # Crear tabla de productos
    cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
                        id INTEGER PRIMARY KEY,
                        nombre TEXT NOT NULL,
                        categoria TEXT NOT NULL,
                        precio REAL NOT NULL
                    )''')

    # Insertar datos de ejemplo
    productos = [
        ('Laptop', 'Electrónica', 1200.50),
        ('Smartphone', 'Electrónica', 800.75),
        ('Camiseta', 'Ropa', 25.99),
        ('Pantalón', 'Ropa', 39.99),
        ('Libro', 'Librería', 15.50),
        ('Bolígrafo', 'Oficina', 1.99)
    ]
    cursor.executemany('INSERT INTO productos (nombre, categoria, precio) VALUES (?, ?, ?)', productos)

    conn.commit()
    conn.close()


# Función para conectar con la base de datos
def conectar_bd(nombre_bd):
    conn = sqlite3.connect(nombre_bd)
    return conn


# Función para ejecutar una consulta SQL y obtener resultados
def ejecutar_consulta(conn, consulta):
    cursor = conn.execute(consulta)
    resultados = cursor.fetchall()
    cursor.close()
    return resultados


# Función para buscar productos por nombre
def buscar_por_nombre(conn, nombre_producto):
    consulta = f"SELECT * FROM productos WHERE nombre LIKE '%{nombre_producto}%'"
    resultados = ejecutar_consulta(conn, consulta)
    return resultados


# Función para buscar productos por categoría
def buscar_por_categoria(conn, categoria):
    consulta = f"SELECT * FROM productos WHERE categoria = '{categoria}'"
    resultados = ejecutar_consulta(conn, consulta)
    return resultados


# Función para buscar productos por rango de precios
def buscar_por_rango_precio(conn, precio_min, precio_max):
    consulta = f"SELECT * FROM productos WHERE precio BETWEEN {precio_min} AND {precio_max}"
    resultados = ejecutar_consulta(conn, consulta)
    return resultados


# Función principal para realizar búsquedas comparativas
def agente_inteligente_busqueda(nombre_bd):
    # Conectar con la base de datos
    conn = conectar_bd(nombre_bd)

    # Ejemplos de consultas
    nombre_producto = 'Laptop'
    categoria = 'Ropa'
    precio_min = 10.0
    precio_max = 50.0

    # Realizar búsquedas y mostrar resultados
    resultados_nombre = buscar_por_nombre(conn, nombre_producto)
    print(f'Resultados para "{nombre_producto}":')
    for producto in resultados_nombre:
        print(producto)
    print('---')

    resultados_categoria = buscar_por_categoria(conn, categoria)
    print(f'Resultados en la categoría "{categoria}":')
    for producto in resultados_categoria:
        print(producto)
    print('---')

    resultados_precio = buscar_por_rango_precio(conn, precio_min, precio_max)
    print(f'Resultados en el rango de precios ${precio_min} - ${precio_max}:')
    for producto in resultados_precio:
        print(producto)

    # Cerrar la conexión con la base de datos
    conn.close()


# Función principal para inicializar y ejecutar el agente
def main():
    nombre_bd = 'mi_base_de_datos.db'  # Nombre de la base de datos SQLite

    # Inicializar la base de datos con datos de ejemplo
    inicializar_base_datos(nombre_bd)

    # Ejecutar el agente inteligente de búsqueda
    agente_inteligente_busqueda(nombre_bd)


# Ejecutar el script
if __name__ == '__main__':
    main()
