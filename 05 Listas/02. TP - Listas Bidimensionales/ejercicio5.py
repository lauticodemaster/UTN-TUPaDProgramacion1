# Escribe un programa que encuentre el valor más grande en una lista bidimensional - Nicolas Ibañez
#  Creamos una lista bidimensional (lista dentro de otra lista)
# Imaginemos que es como una tabla con filas y columnas
numeros = [
    [3, 7, 2],
    [8, 1, 4],
    [6, 9, 5]
]

# Suponemos que el primer número es el más grande( se puede hacer tambien con el ultimo el orden que queramos pero para mas facilidad recomiendo el primero)
mayor = numeros[0][0]

#  Recorremos cada fila
for fila in numeros:
    #  Recorremos cada número dentro de la fila
    for num in fila:
        # Si encontramos un número más grande, lo guardamos en "mayor"(almacenamos basicamente asi hasta q recorra toda la fila y no detecte algo mas mayor)
        if num > mayor:
            mayor = num

#  Mostramos el resultado
print("La lista es:", numeros)
print("El número más grande es:", mayor)