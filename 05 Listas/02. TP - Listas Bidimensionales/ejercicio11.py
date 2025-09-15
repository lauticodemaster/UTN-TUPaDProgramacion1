# Escribe un programa que gire una lista bidimensional (matriz) 90 grados en el sentido 
# de las agujas del reloj - Nicolás Ibañez 

#  Definimos una matriz de ejemplo (lista de listas)
# Es como una tabla de números
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#  Mostramos la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

#  Preparamos una nueva lista vacía donde guardaremos la matriz girada
matriz_girada = []

#  Recorremos la matriz original por columnas
# (porque las columnas se van a transformar en filas)
for j in range(len(matriz[0])):  # len(matriz[0]) = cantidad de columnas
    nueva_fila = []  # fila vacía que vamos a ir llenando
    # Recorremos de abajo hacia arriba
    for i in range(len(matriz) - 1, -1, -1):  
        nueva_fila.append(matriz[i][j])
    matriz_girada.append(nueva_fila)

#  Mostramos la matriz girada
print("\nMatriz girada 90°:")
for fila in matriz_girada:
    print(fila)


