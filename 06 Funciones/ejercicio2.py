# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”.
# Llamar a esta función desde el programa principal solicitando el nombre al usuario.

def generar_saludo(nombre):
    return f"Hola {nombre}!"

nombre_ingresado = input("Ingrese su nombre: ")

mensaje_saludo = generar_saludo(nombre_ingresado)

print(mensaje_saludo)
