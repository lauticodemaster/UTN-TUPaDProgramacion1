# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
# range

multiplos_cuatro = list(range(1, 101))

for n in multiplos_cuatro:
    if n % 4 == 0:
        print(n)
