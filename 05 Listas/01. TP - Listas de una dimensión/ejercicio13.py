# Explique y ejemplifique la librería NumPy para trabajar con matrices y 
# arrays - Lautaro Fernández 

import numpy as np  # Traemos NumPy para poder usar arrays

# -------------------------
# Ejemplo 1: Array simple
# -------------------------
mis_numeros = np.array([1, 2, 3, 4])
print("Mi array 1D:", mis_numeros)

# -------------------------
# Ejemplo 2: Matriz 2x2
# -------------------------
mi_matriz = np.array([[1, 2],
                      [3, 4]])
print("Mi matriz 2x2:\n", mi_matriz)

# -------------------------
# Operaciones entre arrays
# -------------------------
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Suma a+b:", a + b)
print("Resta b-a:", b - a)
print("Multiplicación a*b:", a * b)
print("División b/a:", b / a)

# -------------------------
# Funciones útiles
# -------------------------
numeros = np.array([5, 10, 15, 20])

print("Suma total:", np.sum(numeros))
print("Promedio:", np.mean(numeros))
print("Máximo:", np.max(numeros))
print("Mínimo:", np.min(numeros))

# -------------------------
# Matriz 3x3 ejemplo
# -------------------------
matriz3x3 = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])

# Suma por filas
print("Suma de filas:", np.sum(matriz3x3, axis=1))

# Suma por columnas
print("Suma de columnas:", np.sum(matriz3x3, axis=0))

# Promedio de toda la matriz
print("Promedio matriz:", np.mean(matriz3x3))
