#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

valor1 = int(input("Ingrese el primer número: "))
valor2 = int(input("Ingrese el segundo número: "))

suma_total = 0
menor = min(valor1, valor2)
mayor = max(valor1, valor2)

for n in range(menor + 1, mayor):
    suma_total += n

print(f"La suma de los números entre {menor} y {mayor} es: {suma_total}")
