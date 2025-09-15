# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = int(input("Ingrese un número entero: "))
invertido = 0

while num != 0:
    cifra = num % 10
    invertido = invertido * 10 + cifra
    num //= 10

print(f"Número invertido: {invertido}")
