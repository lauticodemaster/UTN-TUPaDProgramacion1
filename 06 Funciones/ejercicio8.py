# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def obtener_imc(peso_kg, altura_m):
    return round(peso_kg / altura_m**2, 2)

peso_usuario = float(input("Ingrese su peso en kilogramos: "))
altura_usuario = float(input("Ingrese su altura en metros: "))

resultado_imc = obtener_imc(peso_usuario, altura_usuario)

print(f"Su índice de masa corporal (IMC) es: {resultado_imc}")
