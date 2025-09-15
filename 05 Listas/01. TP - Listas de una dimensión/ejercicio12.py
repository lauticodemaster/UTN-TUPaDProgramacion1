# Escribe un programa que sume dos listas de números elemento por elemento. - Luciano Nicolas Ibañez
# Las listas deben tener la misma longitud - 
# Programa: Sumar dos listas de números elemento por elemento

# Pedimos al usuario que ingrese la primera lista
# El usuario escribe números separados por espacio, ejemplo: 1 2 3
entrada1 = input("Ingrese la primera lista de números: ")
# Convertimos la entrada en una lista de números enteros(por las dudas para simplificarla capaz pone 1,5 y se rompe todo)
lista1 = [int(x) for x in entrada1.split()]

# Pedimos al usuario que ingrese la segunda lista
entrada2 = input("Ingrese la segunda lista de números: ")
lista2 = [int(x) for x in entrada2.split()]

# Revisamos que las dos listas tengan la misma cantidad de elementos(Esto muy importante)
if len(lista1) != len(lista2):
    print("Error: Las dos listas deben tener la misma cantidad de números.")
else:
    # Creamos una lista vacía para guardar los resultados(basicamente no pueden unirse o bueno si se unen pero forman una nueva lista asi q si o si debemos crear otra)
    suma = []

    # Recorremos las listas posición por posición(para q vayan bien y mas facil ver el error)
    # y sumamos los elementos que estén en la misma posición
    for i in range(len(lista1)):
        resultado = lista1[i] + lista2[i]   # suma de los dos números
        suma.append(resultado)              # lo guardamos en la nueva lista

    # Mostramos todo
    print("Lista 1:", lista1)
    print("Lista 2:", lista2)
    print("Suma de las dos listas:", suma)
