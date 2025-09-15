# Modifica el programa anterior para que imprima la suma de cada fila de la lista 
# bidimensional. - Maximiliano Reinoso
# Creamos una lista bidimensional (puede ser manual o pedida al usuario)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Mostramos la matriz completa
print("Matriz:")
for fila in matriz:
    print(fila)

print("\nSuma de cada fila:")

# Recorremos cada fila y sumamos sus elementos
for i in range(len(matriz)):
    suma = sum(matriz[i])
    print(f"Fila {i} → suma = {suma}")
