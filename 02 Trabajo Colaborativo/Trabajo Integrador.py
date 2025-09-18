# PRACTICA INTEGRADORA 1 – PYTHON
# --------------------------------

# ---------------------------
# DATOS INICIALES
# ---------------------------

golosinas = [
    [1, "KitKat", 20],
    [2, "Chicles", 50],
    [3, "Caramelos de Menta", 50],
    [4, "Huevo Kinder", 10],
    [5, "Chetoos", 10],
    [6, "Twix", 10],
    [7, "M&M'S", 10],
    [8, "Papas Lays", 2],
    [9, "Milkybar", 10],
    [10, "Alfajor Tofi", 15],
    [11, "Lata Coca", 20],
    [12, "Chitos", 10]
]

empleados = {
    1100: "José Alonso",
    1200: "Federico Pacheco",
    1300: "Nelson Pereira",
    1400: "Osvaldo Tejada",
    1500: "Gastón Garcia"
}

clavesTecnico = ("admin", "CCCDDD", "2020")

golosinasPedidas = []  # [codigo, nombre, cantidad]


# ---------------------------
# FUNCIONES BÁSICAS
# ---------------------------

def mostrar_golosinas():
    print("\n--- LISTA DE GOLOSINAS ---")
    for fila in golosinas:
        print("Código:", fila[0], "|", fila[1], "| Stock:", fila[2])
    print("--------------------------")


def buscar_golosina(codigo):
    for fila in golosinas:
        if fila[0] == codigo:
            return fila
    return None


def registrar_pedido(codigo, nombre):
    existe = False
    for fila in golosinasPedidas:
        if fila[0] == codigo:
            fila[2] = fila[2] + 1
            existe = True
    if not existe:
        golosinasPedidas.append([codigo, nombre, 1])


def pedir_golosina():
    legajo = int(input("Ingrese legajo: "))
    if legajo not in empleados:
        print("Usted no es un empleado de la empresa.")
        return

    mostrar_golosinas()

    codigo = int(input("Ingrese código de golosina (0 para salir): "))
    while codigo != 0:
        g = buscar_golosina(codigo)
        if g == None:
            print("Código inexistente.")
        else:
            if g[2] > 0:
                g[2] = g[2] - 1
                print("Se entregó:", g[1])
                registrar_pedido(g[0], g[1])
            else:
                print("No hay stock de", g[1])
        codigo = int(input("Ingrese código de golosina (0 para salir): "))


def rellenar_golosinas():
    print("Ingrese las 3 claves del técnico")
    c1 = input("Clave 1: ")
    c2 = input("Clave 2: ")
    c3 = input("Clave 3: ")

    if (c1, c2, c3) != clavesTecnico:
        print("No tiene permiso para recargar.")
        return

    mostrar_golosinas()
    codigo = int(input("Ingrese código de golosina: "))
    g = buscar_golosina(codigo)
    if g == None:
        print("Código inexistente.")
    else:
        cantidad = int(input("Ingrese cantidad a recargar: "))
        if cantidad > 0:
            g[2] = g[2] + cantidad
            print("Se recargó", cantidad, "de", g[1], "→ Stock:", g[2])
        else:
            print("Cantidad no válida.")


def apagar_maquina():
    print("\n--- HISTORIAL DE PEDIDOS ---")
    total = 0
    for fila in golosinasPedidas:
        print(fila[1], "| Pedidas:", fila[2])
        total = total + fila[2]
    print("TOTAL DE GOLOSINAS PEDIDAS:", total)
    print("Apagando máquina...")
    exit

# ---------------------------
# MENÚ PRINCIPAL
# ---------------------------

while True:
    print("\n==============================")
    print("       MENÚ PRINCIPAL")
    print("==============================")
    print("a) Pedir golosina")
    print("b) Mostrar golosinas")
    print("c) Rellenar golosinas (técnico)")
    print("d) Apagar máquina")

    opcion = input("Opción: ").lower()

    if opcion == "a":
        pedir_golosina()
    elif opcion == "b":
        mostrar_golosinas()
    elif opcion == "c":
        rellenar_golosinas()
    elif opcion == "d":
        apagar_maquina()
    else:
        print("Opción inválida.")
