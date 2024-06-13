import random


# Definir la función objetivo
def objective_function(x, y):
    return (x ** 2 + y ** 2)


# Definir el rango de búsqueda para x y y
x_range = (-10, 10)
y_range = (-10, 10)

# Inicializar los mejores valores y su puntuación
best_x = None
best_y = None
best_score = float('-inf')

# Realizar búsqueda aleatoria
num_iterations = 100
for _ in range(num_iterations):
    # Generar valores aleatorios para x e y dentro de sus rangos respectivos
    x = random.uniform(x_range[0], x_range[1])
    y = random.uniform(y_range[0], y_range[1])

    # Calcular el valor de la función objetivo
    score = objective_function(x, y)

    # Actualizar los mejores valores encontrados si es necesario
    if score > best_score:
        best_score = score
        best_x = x
        best_y = y

# Imprimir los resultados
print(f"Mejor valor encontrado de x: {best_x:.2f}")
print(f"Mejor valor encontrado de y: {best_y:.2f}")
print(f"Valor máximo de la función objetivo: {best_score:.2f}")
