# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima:
# “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”.
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def mostrar_informacion(nombre, apellido, edad, ciudad):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {ciudad}")

print("Por favor, ingrese sus datos personales:")
nombre_usuario = input("Nombre: ")
apellido_usuario = input("Apellido: ")
edad_usuario = int(input("Edad: "))
ciudad_usuario = input("Residencia: ")

mostrar_informacion(nombre_usuario, apellido_usuario, edad_usuario, ciudad_usuario)
