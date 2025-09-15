# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor)

total_numeros = 5  # Cambiar a 100 para el caso completo
suma = 0

for i in range(1, total_numeros + 1):
    valor = int(input(f"Ingrese el número {i}: "))
    suma += valor

media = suma / total_numeros
print(f"La media de los números ingresados es: {media}")
