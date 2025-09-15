# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo.
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo.
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados

import math

def area_circulo(r):
    return round(math.pi * r**2, 2)

def perimetro_circulo(r):
    return round(2 * math.pi * r, 2)

radio_usuario = float(input("Ingrese el valor del radio del círculo: "))

area = area_circulo(radio_usuario)
perimetro = perimetro_circulo(radio_usuario)

print(f"Área: {area} | Perímetro: {perimetro}")
