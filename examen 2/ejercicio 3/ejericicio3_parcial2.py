def generar_combinaciones(n, m):
    # Lista para almacenar todas las combinaciones posibles
    combinaciones = []

    # Función auxiliar recursiva para generar combinaciones
    def generar_combinaciones_rec(actual_combinacion, indice):
        if indice == n:
            # Se ha considerado cada libro
            combinaciones.append(tuple(tuple(espacio) for espacio in actual_combinacion))
            return

        for espacio in range(m):
            # Añadir el libro actual al espacio 'espacio'
            actual_combinacion[espacio].append(indice + 1)
            generar_combinaciones_rec(actual_combinacion, indice + 1)
            # Deshacer la adición para explorar otras combinaciones
            actual_combinacion[espacio].pop()

    # Inicializar la combinación actual con listas vacías para cada espacio
    actual_combinacion = [[] for _ in range(m)]

    # Iniciar la generación de combinaciones
    generar_combinaciones_rec(actual_combinacion, 0)

    return combinaciones



n = 3  #  libros
m = 2  # espacios

todas_combinaciones = generar_combinaciones(n, m)

print(f"Todas las combinaciones posibles para {n} libros en {m} espacios son:")
for combinacion in todas_combinaciones:
    print(combinacion)
