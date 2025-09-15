# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

def convertir_celsius_a_fahrenheit(c):
    return round((c * 1.8) + 32, 2)

temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))

temperatura_fahrenheit = convertir_celsius_a_fahrenheit(temperatura_celsius)

print(f"{temperatura_celsius}°C equivalen a {temperatura_fahrenheit}°F")
