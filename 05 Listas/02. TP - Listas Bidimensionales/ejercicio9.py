# Crea un programa que genere una matriz identidad inversa de tamaño n. Una matriz 
# identidad inversa es una matriz cuadrada donde los elementos de la diagonal inversa
# principal son 1 y el resto son 0. - Maximiliano Reinoso
# Pedimos al usuario el tamaño de la matriz
n = int(input("Ingresa el tamaño de la matriz identidad inversa: "))

# Creamos la matriz identidad inversa
matriz = []

for i in range(n):
    fila = []
    for j in range(n):
        # Usamos la condición para la diagonal inversa
        if i + j == n - 1:
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)

# Mostramos la matriz
print("\nMatriz identidad inversa:")
for fila in matriz:
    print(" ".join(str(x) for x in fila))