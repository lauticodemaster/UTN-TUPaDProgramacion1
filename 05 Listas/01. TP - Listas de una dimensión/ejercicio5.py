# Escribe un programa que multiplique cada elemento de una lista de números por un 
# valor ingresado por el usuario. - Leonel Fanchinelli

#En caso de que todos los numero deban ser dados por el usuario
bandera=1
numero=0
lista=[]
while bandera==1:
    numero=int(input("Ingrese un numero para la lista: "))
    lista.append(numero)
    bandera=int(input("Si desea ingresar otro numero ingrese 1, sino ingrese 0: "))

for i in range (len (lista)):
    lista[i]=lista[i]*int(input("Ingrese un numero para multiplicar la lista: "))
print(lista)

#En caso de que la lista ya este dada

numero=0
lista=[8,2,12,9,5]
for i in range (len (lista)):
    lista[i]=lista[i]*int(input("Ingrese un numero para multiplicar la lista: "))
print(lista)
