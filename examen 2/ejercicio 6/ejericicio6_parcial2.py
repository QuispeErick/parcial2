import numpy as np

# Definición de nodos y aristas con pesos
nodos = ['A', 'B', 'C', 'D', 'E']
aristas = [
    ('A', 'B', 7),
    ('A', 'C', 9),
    ('A', 'D', 8),
    ('A', 'E', 20),
    ('B', 'C', 10),
    ('B', 'D', 4),
    ('B', 'E', 11),
    ('C', 'D', 15),
    ('C', 'E', 5),
    ('D', 'E', 17)
]

# Crear matriz de adyacencia inicializada con ceros
num_nodos = len(nodos)
matriz_adyacencia = np.zeros((num_nodos, num_nodos), dtype=int)

# Llenar matriz de adyacencia con los pesos de las aristas
for inicio, fin, peso in aristas:
    indice_inicio = nodos.index(inicio)
    indice_fin = nodos.index(fin)
    matriz_adyacencia[indice_inicio, indice_fin] = peso
    matriz_adyacencia[indice_fin, indice_inicio] = peso  # Si el grafo es no dirigido, agregar esta línea

# Mostrar matriz de adyacencia
print("Matriz de Adyacencia:")
print(matriz_adyacencia)
