# Escribe un programa que pida al usuario una lista de números y encuentre el mayor y 
# el menor de ellos - Maximiliano Mendez
numeros = int(input("Ingrese una lista de números usando espacios: "))
# Aca queria utilizar el operador split para hacer mas facil la entrada de los numeros
#Despues los introduje a una lista bidimensional
listaNumeros = [int(i) for i in numeros.split()]
# Creamos las variables para los resultados
mayor = listaNumeros[0]
menor = listaNumeros[0]
# Con dichos resultados damos las asignaciones de si son mayor o menorr
for numeros in listaNumeros:
    if numeros > mayor:
        mayor = numeros
    elif numeros < menor:
        menor = numeros
# Ponemos el resultado (:V)
print("El número mayor es:", mayor)
print("El número menor es:", menor)