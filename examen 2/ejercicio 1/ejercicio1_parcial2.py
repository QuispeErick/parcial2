import numpy as np
import pandas as pd


# Cargar y preprocesar el dataset
def cargar_datos(nombre_archivo):
    datos = pd.read_csv(nombre_archivo)
    # Convertir las etiquetas en números
    datos['species'] = datos['species'].astype('category').cat.codes
    X = datos.iloc[:, :-1].values
    y = datos.iloc[:, -1].values
    return X, y


def normalizar(X):
    return (X - X.mean(axis=0)) / X.std(axis=0)


# Definir funciones de activación
def sigmoide(x):
    return 1 / (1 + np.exp(-x))


def derivada_sigmoide(x):
    return x * (1 - x)


# Inicializar pesos
def inicializar_pesos(tamano_entrada, tamano_oculta, tamano_salida):
    W1 = np.random.randn(tamano_entrada, tamano_oculta)
    b1 = np.zeros((1, tamano_oculta))
    W2 = np.random.randn(tamano_oculta, tamano_salida)
    b2 = np.zeros((1, tamano_salida))
    return W1, b1, W2, b2


# Proceso de entrenamiento
def entrenar(X, y, tamano_oculta, epocas, tasa_aprendizaje):
    tamano_entrada = X.shape[1]
    tamano_salida = len(np.unique(y))
    W1, b1, W2, b2 = inicializar_pesos(tamano_entrada, tamano_oculta, tamano_salida)
    y_onehot = np.eye(tamano_salida)[y]

    for epoca in range(epocas):
        # Paso hacia adelante
        Z1 = np.dot(X, W1) + b1
        A1 = sigmoide(Z1)
        Z2 = np.dot(A1, W2) + b2
        A2 = sigmoide(Z2)

        # Cálculo de la pérdida (Error Cuadrático Medio)
        perdida = np.mean((A2 - y_onehot) ** 2)

        if epoca % 10000 == 0:
            print(f'Época {epoca}, Pérdida: {perdida}')

        # Retropropagación
        dA2 = 2 * (A2 - y_onehot) / y.size
        dZ2 = dA2 * derivada_sigmoide(A2)
        dW2 = np.dot(A1.T, dZ2)
        db2 = np.sum(dZ2, axis=0, keepdims=True)

        dA1 = np.dot(dZ2, W2.T)
        dZ1 = dA1 * derivada_sigmoide(A1)
        dW1 = np.dot(X.T, dZ1)
        db1 = np.sum(dZ1, axis=0, keepdims=True)

        # Actualización de parámetros mediante descenso de gradiente
        W1 -= tasa_aprendizaje * dW1
        b1 -= tasa_aprendizaje * db1
        W2 -= tasa_aprendizaje * dW2
        b2 -= tasa_aprendizaje * db2

    return W1, b1, W2, b2


# Predicción
def predecir(X, W1, b1, W2, b2):
    Z1 = np.dot(X, W1) + b1
    A1 = sigmoide(Z1)
    Z2 = np.dot(A1, W2) + b2
    A2 = sigmoide(Z2)
    return np.argmax(A2, axis=1)


# Cargar y preparar los datos
X, y = cargar_datos('iris.csv')
X = normalizar(X)

# Entrenar la red neuronal
tamano_oculta = 5
epocas = 1000000
tasa_aprendizaje = 0.4

W1, b1, W2, b2 = entrenar(X, y, tamano_oculta, epocas, tasa_aprendizaje)

# Evaluar el modelo
predicciones = predecir(X, W1, b1, W2, b2)
precision = np.mean(predicciones == y)
print(f'Precisión: {precision}')
