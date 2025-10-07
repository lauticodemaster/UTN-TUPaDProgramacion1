
# Diccionario de alumnos (legajo: nombre)
alumnos = {
    60902: "Rodolfo Fernandez",
    61654: "Luis Gomez",
    61852: "Andrea Pereira",
    61754: "Juan Cruz Gonzales"
}

# Lista para guardar promedios generales
notasFinales = [
    ["Rodolfo Fernandez"],
    ["Luis Gomez"],
    ["Andrea Pereira"],
    ["Juan Cruz Gonzales"]
]

# -------- FUNCIONES -------- #

def pedir_notas():
    """Pide dos notas, valida que estén entre 0 y 10 y devuelve promedio"""
    while True:
        try:
            n1 = float(input("Nota 1: "))
            n2 = float(input("Nota 2: "))
            if 0 <= n1 <= 10 and 0 <= n2 <= 10:
                prom = round((n1 + n2) / 2, 2)
                return n1, n2, prom
            else:
                print(" Las notas deben estar entre 0 y 10. Intente de nuevo.")
        except:
            print(" Entrada inválida. Use números.")

# -------- PROGRAMA PRINCIPAL -------- #

for legajo in alumnos:   # Iteramos los alumnos
    nombre = alumnos[legajo]
    print(f"\nAlumno/a: {nombre} - Legajo: {legajo}")

    # Lista de materias (Materia, Nota1, Nota2, Promedio)
    materias = [
        ["Ciencias"],
        ["Historia"],
        ["Geografía"],
        ["Matemáticas"],
        ["Física"]
    ]

    # Cargar notas de cada materia
    for materia in materias:
        print(f"\nIngrese notas para {materia[0]}:")
        n1, n2, prom = pedir_notas()
        materia.append(n1)
        materia.append(n2)
        materia.append(prom)

    # Mostrar la tabla de materias
    print("\n---------------------------------")
    for m in materias:
        print(f"{m[0]} | Nota1: {m[1]} | Nota2: {m[2]} | Final: {m[3]}")
    print("---------------------------------")

    # Determinar materia con mejor promedio
    mejor = max(materias, key=lambda x: x[3])
    print(f"📌 Mejor materia: {mejor[0]} con {mejor[3]}")

    # Calcular promedio general
    suma = 0
    for m in materias:
        suma += m[3]
    promedioGeneral = round(suma / len(materias), 2)

    # Guardar en notasFinales
    for fila in notasFinales:
        if fila[0] == nombre:
            fila.append(promedioGeneral)
            break

    print(f"Promedio general de {nombre}: {promedioGeneral}")

# Al terminar todos los alumnos, mostrar lista de promedios
print("\n===== PROMEDIOS FINALES =====")
for fila in notasFinales:
    print(f"{fila[0]} -> {fila[1]}")

# Determinar mejor promedio de todos
mejorAlumno = max(notasFinales, key=lambda x: x[1])
print(f"\n🏆 El mejor promedio es {mejorAlumno[1]} de {mejorAlumno[0]}")

