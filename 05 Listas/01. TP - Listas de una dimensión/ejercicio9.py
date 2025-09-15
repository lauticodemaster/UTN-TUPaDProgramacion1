# Escribe un programa que permita al usuario ingresar una lista de números y filtre los 
# números primos. - Mailen Ortiz

lista = [] #Lista vacía para que luego el usuario ingrese los números y se guarden acá
cantidadNumeros = int(input("Ingrese la cantidad de números que quiere agregar: "))

#Se crea la lista original, con todos los números ingresados
for contador in range(cantidadNumeros):
    numero = int(input(f"Ingrese el elemento {contador +1}: ")) #El usuario ingresa el valor
    lista.append(numero)

listaPrimos = [] #Lista vacía para agregar luego los números primos

for valor in lista: #Recorro toda la lista
    if valor > 1:
        divisores = 0
        for contador in range(2, valor): #No incluyo 1 ni el mismo número, ya que solo quiero saber si se obtiene resto 0 al dividirlo con los demás
            if valor % contador == 0:
                primo += 1
        if primo == 0: #Si no se encuentra ningún divisor, es primo y se agrega a la listaPrimos
            listaPrimos.append(valor) 

print(f"De la lista ingresada los números: {listaPrimos} son primos")



