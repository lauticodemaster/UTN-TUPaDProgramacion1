# Escribe un programa que multiplique cada elemento de una lista bidimensional por un 
# valor escalar dado por el usuario. - Lautaro Fernández

# Paso 1: Definimos una lista bidimensional (matriz)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Mostramos la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Paso 2: Pedimos al usuario el valor escalar
escalar = float(input("Ingresa un valor escalar para multiplicar la matriz: "))

# Paso 3: Creamos una nueva matriz para guardar los resultados
matriz_resultado = []

# Paso 4: Multiplicamos cada elemento por el escalar
for fila in matriz:
    nueva_fila = []
    for elemento in fila:
        nueva_fila.append(elemento * escalar)
    matriz_resultado.append(nueva_fila)

# Paso 5: Mostramos la matriz resultante
print("Matriz después de multiplicar por el escalar:")
for fila in matriz_resultado:
    print(fila)
