# Escribe un programa que pida al usuario una lista de números y cuente cuántos de 
# ellos son pares y cuántos son impares - Maximiliano Reinoso
# Pedimos al usuario que escriba una lista de números separados por comas
entrada = input("Escribe una lista de números separados por comas: ")

# Separamos los números usando split(",") y los convertimos en enteros
numeros = [int(num) for num in entrada.split(",")]

# Creamos dos variables para contar pares e impares
pares = 0
impares = 0

# Recorremos la lista de números
for numero in numeros:
    if numero % 2 == 0:
        pares += 1  # Si el número es divisible por 2, es par
    else:
        impares += 1  # Si no, es impar

# Mostramos los resultados
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
