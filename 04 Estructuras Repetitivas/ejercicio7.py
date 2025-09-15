# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

limite = int(input("Ingrese un número entero positivo: "))
suma_total = 0

if limite >= 0:
    for n in range(limite + 1):
        suma_total += n
    print(f"La suma de los números desde 0 hasta {limite} es: {suma_total}")
else:
    print("Número inválido. Debe ingresar un número positivo.")
