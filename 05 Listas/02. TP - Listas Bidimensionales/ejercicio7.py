# Escribe un programa que extraiga los elementos de la diagonal principal de una matriz 
# cuadrada. - Maximiliano Mendez
# Pedir el tamaño de la matriz cuadrada
n = int(input("Ingrese el tamaño de la matriz cuadrada: "))

# Crear la matriz vacía
matriz = []
i = 0
# en sta sección puse un bucle for anidado con un bucle while para llenar la matriz
for i in range(n): # El rango de la matriz
    while True:
        # If para no cometer error
        fila = input(f"Ingrese los {n} elementos de la fila {i+1} separados por espacio: ").split()
        if len(fila) != n:
            print(f"Debe ingresar exactamente {n} elementos.")
            continue
        break # Detengo el bucle por completo ñañaña
    matriz.append(fila)

# Sacamos los elementos de la diagonal principal
diagonal = [matriz[i][i] for i in range(n)]

# Los mostramos 
print("Elementos de la diagonal principal:", diagonal)
