# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos.
# Mostrar los resultados de forma clara.

def calcular_operaciones(a, b):
    return (a + b, a - b, a * b, a / b)

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

suma, resta, multiplicacion, division = calcular_operaciones(num1, num2)

print(f"""Resultados de las operaciones:
    Suma = {suma}
    Resta = {resta}
    Multiplicación = {multiplicacion}
    División = {division}
""")
