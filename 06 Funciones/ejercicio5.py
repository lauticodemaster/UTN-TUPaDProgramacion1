# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def convertir_segundos_a_horas(seg):
    return round(seg / 3600, 2)

segundos_usuario = int(input("Ingrese la cantidad de segundos: "))

horas = convertir_segundos_a_horas(segundos_usuario)

print(f"{segundos_usuario} segundos equivalen a {horas} hora/s")
