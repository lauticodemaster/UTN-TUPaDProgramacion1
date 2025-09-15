# Escribe un programa que permita al usuario ingresar una lista de números y calcule el 
# promedio de los elementos - Lautaro Fernández

numeros = [0] * 100   # lista con espacio reservado
suma_total = 0
contador = 0

dato = input("Ingresa un número (o 'fin' para terminar): ")

while dato != "fin":
    numero = int(dato)
    numeros[contador] = numero
    suma_total = suma_total + numero
    contador = contador + 1
    dato = input("Ingresa un número (o 'fin' para terminar): ")

if contador > 0:
    promedio = suma_total / contador
    print("El promedio de los números es:", promedio)
else:
    print("No ingresaste ningún número.")

