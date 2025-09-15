# Escribe un programa que calcule la suma de todos los elementos en una lista 
# bidimensional - Mailen Ortiz

#Se crea una lista con los valores para sumar
lista = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#Recorre cada sublista dentro de la lista principal luego recorre cada número de la fila y suma todos los valores.

suma = 0

for fila in lista:
    for numero in fila:
        suma += numero

print(f"La suma de todos los elementos es: {suma}") 