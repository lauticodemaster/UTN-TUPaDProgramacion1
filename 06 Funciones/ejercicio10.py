# 10. Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta función.

def promedio_tres_numeros(x, y, z):
    return (x + y + z) / 3

print("Ingrese tres números para calcular su promedio:")

num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))
num3 = float(input("Número 3: "))

resultado_promedio = promedio_tres_numeros(num1, num2, num3)

print(f"El promedio de los números {num1}, {num2} y {num3} es: {resultado_promedio}")
