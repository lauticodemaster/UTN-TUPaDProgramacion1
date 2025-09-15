#6) Escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

import random
from statistics import mean, median, mode

valores = [random.randint(1, 100) for _ in range(50)]

moda_val = mode(valores)
mediana_val = median(valores)
media_val = mean(valores)

print("Lista generada:", valores)
print("Moda:", moda_val)
print("Mediana:", mediana_val)
print("Media:", media_val)

if media_val > mediana_val > moda_val:
    print("Sesgo positivo")
elif media_val < mediana_val < moda_val:
    print("Sesgo negativo")
elif media_val == mediana_val == moda_val:
    print("No hay sesgo")
else:
    print("No se pudo determinar el sesgo con los valores actuales")
