# ---------------------------
# DATOS INICIALES
# ---------------------------
# Lista de golosinas, donde cada elemento es una lista con [codigo, nombre, stock]
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

# Diccionario de empleados donde la clave es el legajo y el valor es el nombre del empleado.
empleados = {
    1100: "José Alonso",
    1200: "Federico Pacheco",
    1300: "Nelson Pereira",
    1400: "Osvaldo Tejada",
    1500: "Gastón Garcia"
}

# Claves de técnico necesarias para recargar stock de golosinas
clavesTecnico = ("admin", "CCCDDD", "2020")

# Lista para almacenar los pedidos de golosinas
golosinasPedidas = []  # [codigo, nombre, cantidad]


# ---------------------------
# FUNCIONES BÁSICAS
# ---------------------------

# Muestra todas las golosinas disponibles con su código y stock
def mostrar_golosinas():
    print("\n--- LISTA DE GOLOSINAS ---")
    for fila in golosinas:
        print("Código:", fila[0], "|", fila[1], "| Stock:", fila[2])
    print("--------------------------")

# Busca una golosina por su código. Si no existe, devuelve None.
def buscar_golosina(codigo):
    for fila in golosinas:
        if fila[0] == codigo:
            return fila
    return None

# Registra un pedido, aumentando la cantidad si ya existe el producto en los pedidos
def registrar_pedido(codigo, nombre):
    existe = False
    for fila in golosinasPedidas:
        if fila[0] == codigo:
            fila[2] = fila[2] + 1
            existe = True
    if not existe:
        golosinasPedidas.append([codigo, nombre, 1])

# Permite a un empleado pedir una golosina
def pedir_golosina():
    legajo = int(input("Ingrese legajo: "))
    # Verifica si el legajo es válido
    if legajo not in empleados:
        print("Usted no es un empleado de la empresa.")
        return

    mostrar_golosinas()

    codigo = int(input("Ingrese código de golosina (0 para salir): "))
    while codigo != 0:
        g = buscar_golosina(codigo)
        # Si no existe la golosina, muestra un mensaje
        if g == None:
            print("Código inexistente.")
        else:
            if g[2] > 0:
                # Si hay stock, reduce uno y registra el pedido
                g[2] = g[2] - 1
                print("Se entregó:", g[1])
                registrar_pedido(g[0], g[1])
            else:
                print("No hay stock de", g[1])
        codigo = int(input("Ingrese código de golosina (0 para salir): "))

# Permite al técnico recargar el stock de las golosinas
def rellenar_golosinas():
    print("Ingrese las 3 claves del técnico")
    c1 = input("Clave 1: ")
    c2 = input("Clave 2: ")
    c3 = input("Clave 3: ")

    # Verifica si las claves son correctas
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
            # Si la cantidad es válida, se recarga el stock
            g[2] = g[2] + cantidad
            print("Se recargó", cantidad, "de", g[1], "→ Stock:", g[2])
        else:
            print("Cantidad no válida.")

# Apaga la máquina y muestra un resumen de los pedidos realizados
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

# Bucle principal del menú
while True:
    print("\n==============================")
    print("       MENÚ PRINCIPAL")
    print("==============================")
    print("a) Pedir golosina")
    print("b) Mostrar golosinas")
    print("c) Rellenar golosinas (técnico)")
    print("d) Apagar máquina")

    opcion = input("Opción: ").lower()

    # Si la opción es 'a', pide una golosina
    if opcion == "a":
        pedir_golosina()
    # Si la opción es 'b', muestra las golosinas disponibles
    elif opcion == "b":
        mostrar_golosinas()
    # Si la opción es 'c', permite a un técnico recargar stock
    elif opcion == "c":
        rellenar_golosinas()
    # Si la opción es 'd', apaga la máquina
    elif opcion == "d":
        apagar_maquina()
    # Si la opción es inválida, muestra un mensaje
    else:
        print("Opción inválida.")
