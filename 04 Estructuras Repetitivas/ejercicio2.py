#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

numero = int(input("Ingrese un número entero: "))
numero = abs(numero)
digitos = 0

if numero == 0:
    digitos = 1
else:
    digitos = 0
    while numero > 0:
        numero //= 10
        digitos += 1

print(f"El número contiene {digitos} digitos.")

