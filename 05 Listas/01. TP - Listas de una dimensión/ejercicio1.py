# Escribe un programa que permita al usuario ingresar una lista de números y calcule la 
# suma de todos los elementos en la lista - Lautaro Fernández

# Paso 1: Definimos la lista (cargada a mano)
numeros = [3, 7, 2, 5, 10]

# Paso 2: Creamos variables de control
i = 0            # índice para recorrer la lista
suma_total = 0   # acumulador
cantidad = 5     # cantidad de elementos que tiene la lista

# Paso 3: Bucle manual para recorrer la lista
while i < cantidad:
    suma_total = suma_total + numeros[i]  # sumamos el número actual
    i = i + 1                             # pasamos al siguiente índice

# Paso 4: Mostramos el resultado
print("La suma de los números es:", suma_total)
