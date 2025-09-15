#  Encontrar el número más grande en una lista bidimensional (con datos del usuario)

# Paso 1: Pedimos cuántas filas y columnas tendrá la lista
filas = int(input("¿Cuántas filas tendrá la lista? "))
columnas = int(input("¿Cuántas columnas tendrá la lista? "))

# Paso 2: Creamos una lista vacía donde vamos a guardar todo
numeros = []

# Paso 3: Usamos un bucle para ir llenando la lista fila por fila
for i in range(filas):
    fila = []  # lista vacía para cada fila
    for j in range(columnas):
        num = int(input(f"Ingrese un número para la posición ({i}, {j}): "))
        fila.append(num)  # agregamos el número a la fila
    numeros.append(fila)  # guardamos la fila dentro de la lista principal

# Paso 4: Suponemos que el primer número es el mayor
mayor = numeros[0][0]

# Paso 5: Recorremos toda la lista para buscar el más grande
for fila in numeros:
    for num in fila:
        if num > mayor:
            mayor = num

# Paso 6: Mostramos los resultados
print("La lista es:", numeros)
print("El número más grande es:", mayor)
