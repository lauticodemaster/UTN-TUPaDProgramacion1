#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

FIN = 0
valor = int(input(f"Ingrese un número entero (0 para terminar): "))
suma_total = 0

while valor != FIN:
    suma_total += valor
    valor = int(input(f"Ingrese otro número (0 para terminar): "))

print(f"La suma total de los números ingresados es: {suma_total}")
