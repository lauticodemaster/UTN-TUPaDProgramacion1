# Crea una función que reciba dos parámetros: el número de filas y columnas. La función 
# debe generar una matriz de ese tamaño, donde los valores son números enteros 
# consecutivos empezando desde 1. - Maximiliano Mendez 

# Pedir el tamaño de las columanas y filas
filas = 0
columnas = 0
# Pongo ciclo while para no tener errores 
while filas < 1:
    filas = int(input("Ingrese el número de filas (1...): "))
while columnas < 1:
 columnas = int(input("Ingrese el número de columnas (1...): "))

# Crear la matriz vacía
matriz = []
contador = 1  # Empezamos desde 1
i = 0
j = 0
# Llenamos de informacion cuchao
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(contador)
        contador += 1
    matriz.append(fila)
    # Este proceso se repite en cada iteración del bucle interno

# Mostramos las columnas y filas
for fila in matriz:
    print(fila)