# Escribe un programa que permita al usuario ingresar una lista de números y eliminar 
# un elemento en un índice especificado. - Maximiliano Reinoso
# Paso 1: Pedimos al usuario que escriba una lista de números separados por comas
entrada = input("Escribe una lista de números separados por comas: ")
numeros = [int(num) for num in entrada.split(",")]

# Mostramos la lista con los índices para que el usuario sepa cuál eliminar
print("Lista original:", numeros)

# Paso 2: Pedimos el índice que quiere eliminar
indice = int(input("Escribe el índice del número que quieres eliminar: "))

# Paso 3: Verificamos si el índice es válido
if 0 <= indice < len(numeros):
    eliminado = numeros.pop(indice)  # Elimina el número en ese índice
    print(f"Se eliminó el número: {eliminado}")
else:
    print("Índice fuera de rango. No se eliminó ningún número.")

# Paso 4: Mostramos la lista actualizada
print("Lista actualizada:", numeros)
