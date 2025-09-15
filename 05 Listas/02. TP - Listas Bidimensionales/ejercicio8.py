# Crea un programa que genere una matriz identidad de tamaño n. Una matriz identidad 
# es una matriz cuadrada donde los elementos de la diagonal principal son 1 y el resto 
# son 0. - Mailen Ortiz

#Se le pide al usuario que ingrese el tamaño de la matriz
tamañoMatriz = int(input("Ingrese el tamaño de la matriz identidad:"))

#Recorre filas y columnas, si el índice de la fila es igual al de la columna coloca un 1 y sino un 0
matrizIdentidad =  [[1 if i == j else 0 for j in range(tamañoMatriz)] for i in range(tamañoMatriz)]

#Muestra el resultado
print("Matriz Identidad:")
for fila in matrizIdentidad:
    print(fila)
