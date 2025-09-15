# Escribe un programa que permita al usuario ingresar una lista y un número, y cuente 
# cuántas veces aparece ese número en la lista - Leonel Fanchinelli
bandera=1
numero=0
contador=0
lista=[]

while bandera==1:
    numero=int(input("Ingrese un numero para la lista: "))
    lista.append(numero)
    bandera=int(input("Si desea ingresar otro numero ingrese 1, sino ingrese 0: "))
numero=int(input("Ingrese un numero para buscar en la lista: "))
for i in range (len (lista)):
    if lista[i]==numero:
        contador+=1
print("El numero",numero,"aparece",contador,"veces en la lista")
