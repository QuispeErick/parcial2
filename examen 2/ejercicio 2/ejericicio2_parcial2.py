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
def escalon(x):
    return np.where(x >= 0, 1, 0)


def derivada_escalon(x):
    return np.ones_like(
        x)  # La derivada no es útil para la función escalón en el sentido clásico, pero la necesitamos para el código.


# Inicializar pesos
def inicializar_pesos(tamano_entrada, tamano_oculta, tamano_oculta2, tamano_salida):
    W1 = np.random.randn(tamano_entrada, tamano_oculta)
    b1 = np.zeros((1, tamano_oculta))
    W2 = np.random.randn(tamano_oculta, tamano_oculta2)
    b2 = np.zeros((1, tamano_oculta2))
    W3 = np.random.randn(tamano_oculta2, tamano_salida)
    b3 = np.zeros((1, tamano_salida))
    return W1, b1, W2, b2, W3, b3


# Proceso de entrenamiento
def entrenar(X, y, tamano_oculta, tamano_oculta2, intentos, tasa_aprendizaje):
    tamano_entrada = X.shape[1]
    tamano_salida = len(np.unique(y))
    W1, b1, W2, b2, W3, b3 = inicializar_pesos(tamano_entrada, tamano_oculta, tamano_oculta2, tamano_salida)
    y_onehot = np.eye(tamano_salida)[y]

    for intento in range(intentos):
        # Paso hacia adelante
        Z1 = np.dot(X, W1) + b1
        A1 = escalon(Z1)
        Z2 = np.dot(A1, W2) + b2
        A2 = escalon(Z2)
        Z3 = np.dot(A2, W3) + b3
        A3 = escalon(Z3)

        # Cálculo de la pérdida (Error Cuadrático Medio)
        perdida = np.mean((A3 - y_onehot) ** 2)

        if intento % 100 == 0:
            print(f'Intento {intento}, Pérdida: {perdida}')

        # Retropropagación
        dA3 = 2 * (A3 - y_onehot) / y.size
        dZ3 = dA3 * derivada_escalon(A3)
        dW3 = np.dot(A2.T, dZ3)
        db3 = np.sum(dZ3, axis=0, keepdims=True)

        dA2 = np.dot(dZ3, W3.T)
        dZ2 = dA2 * derivada_escalon(A2)
        dW2 = np.dot(A1.T, dZ2)
        db2 = np.sum(dZ2, axis=0, keepdims=True)

        dA1 = np.dot(dZ2, W2.T)
        dZ1 = dA1 * derivada_escalon(A1)
        dW1 = np.dot(X.T, dZ1)
        db1 = np.sum(dZ1, axis=0, keepdims=True)

        # Actualización de parámetros mediante descenso de gradiente
        W1 -= tasa_aprendizaje * dW1
        b1 -= tasa_aprendizaje * db1
        W2 -= tasa_aprendizaje * dW2
        b2 -= tasa_aprendizaje * db2
        W3 -= tasa_aprendizaje * dW3
        b3 -= tasa_aprendizaje * db3

    return W1, b1, W2, b2, W3, b3


# Predicción
def predecir(X, W1, b1, W2, b2, W3, b3):
    Z1 = np.dot(X, W1) + b1
    A1 = escalon(Z1)
    Z2 = np.dot(A1, W2) + b2
    A2 = escalon(Z2)
    Z3 = np.dot(A2, W3) + b3
    A3 = escalon(Z3)
    return np.argmax(A3, axis=1)


# Cargar y preparar los datos
X, y = cargar_datos('iris.csv')
X = normalizar(X)

# Entrenar la red neuronal
tamano_oculta = 5
tamano_oculta2 = 5
intentos = 1000
tasa_aprendizaje = 0.2

W1, b1, W2, b2, W3, b3 = entrenar(X, y, tamano_oculta, tamano_oculta2, intentos, tasa_aprendizaje)

# Evaluar el modelo
predicciones = predecir(X, W1, b1, W2, b2, W3, b3)
precision = np.mean(predicciones == y)
print(f'Precisión: {precision}')
