# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función

def mostrar_tabla_multiplicar(n):
    print(f"Tabla de multiplicar del {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

numero_usuario = int(input("Ingrese un número para ver su tabla de multiplicar: "))

mostrar_tabla_multiplicar(numero_usuario)
