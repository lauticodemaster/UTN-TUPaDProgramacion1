# Escribe un programa que permita al usuario ingresar una lista de números y elimine los 
# elementos duplicados. - Nicolás Ibañez

# Paso 1: Pedimos los datos correspondientes
entrada = input("Ingrese números separados por espacios: ")

#  Convertimos los datos  (que es texto) en una lista de números
# .split() separa por espacios, y usamos int() para pasarlos a enteros un poco dificil de explicar esto
numeros = [int(x) for x in entrada.split()]


# Ahora tenemos la lista con los numeros q ingresamos
print("Lista original:", numeros)

#  Eliminar duplicados
# La forma fácil es convertir la lista en un conjunto (set), 
# porque los conjuntos NO permiten duplicados
# Después volvemos a lista para que tenga el mismo formato
sin_duplicados = list(set(numeros))

# Paso 4: y ahora mostramos como quedo 
print("Lista sin duplicados:", sin_duplicados)
