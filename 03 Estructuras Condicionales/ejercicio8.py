#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.

usuario = input("Ingrese su nombre: ")

print("""
Seleccione cómo desea mostrar su nombre:
1 - Todo en MAYÚSCULAS
2 - Todo en minúsculas
3 - Solo la primera letra en mayúscula
""")
eleccion = int(input("Ingrese la opción deseada (1/2/3): "))

if eleccion == 1:
    print("Resultado:", usuario.upper())
elif eleccion == 2:
    print("Resultado:", usuario.lower())
elif eleccion == 3:
    print("Resultado:", usuario.title())
else:
    print("Opción ingresada no válida")
