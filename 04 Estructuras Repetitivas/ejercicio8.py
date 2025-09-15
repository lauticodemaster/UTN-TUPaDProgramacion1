# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

total_numeros = 10  # Cambiar a 100 para el caso completo
contador_pares = 0
contador_impares = 0
contador_positivos = 0
contador_negativos = 0

for i in range(1, total_numeros + 1):
    valor = int(input(f"Ingrese el número {i}: "))

    if valor % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1

    if valor >= 0:
        contador_positivos += 1
    else:
        contador_negativos += 1

print(f"""
De los números ingresados:
- Pares: {contador_pares}
- Impares: {contador_impares}
- Positivos: {contador_positivos}
- Negativos: {contador_negativos}
""")
