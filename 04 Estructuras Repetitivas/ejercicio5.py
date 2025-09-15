#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

numero_secreto = random.randint(0, 9)
adivinanza = int(input("Adivina el número entre 0 y 9: "))

contador_intentos = 1

while adivinanza != numero_secreto:
    adivinanza = int(input("¡Incorrecto! Intenta de nuevo: "))
    contador_intentos += 1

print(f"¡Correcto! Número de intentos: {contador_intentos}")
