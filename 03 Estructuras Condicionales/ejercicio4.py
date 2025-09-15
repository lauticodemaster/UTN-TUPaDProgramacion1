#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años

edad_usuario = int(input("Ingrese su edad: "))

if 0 <= edad_usuario < 12:
    print("Perteneces a la categoría Niño/a")
elif 12 <= edad_usuario < 18:
    print("Perteneces a la categoría Adolescente")
elif 18 <= edad_usuario < 30:
    print("Perteneces a la categoría Adulto/a joven")
elif edad_usuario >= 30:
    print("Perteneces a la categoría Adulto/a")
else:
    print("Edad ingresada no válida")
