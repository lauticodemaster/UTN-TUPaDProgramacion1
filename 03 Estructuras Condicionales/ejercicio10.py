#10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

zona = input("Indique el hemisferio (norte/sur): ").lower()
mes_actual = input("Escriba el mes en curso: ").lower()
dia_actual = int(input("Ingrese el día del mes: "))

if dia_actual < 1 or dia_actual > 31:
    print("Día fuera de rango (1 a 31)")
else:
    # ------------------- HEMISFERIO NORTE -------------------
    if zona == "norte":
        if mes_actual in ["enero", "febrero"]:
            print("Estación: Invierno")
        elif mes_actual == "marzo":
            if dia_actual <= 20:
                print("Estación: Invierno")
            else:
                print("Estación: Primavera")
        elif mes_actual in ["abril", "mayo"]:
            print("Estación: Primavera")
        elif mes_actual == "junio":
            if dia_actual <= 20:
                print("Estación: Primavera")
            else:
                print("Estación: Verano")
        elif mes_actual in ["julio", "agosto"]:
            print("Estación: Verano")
        elif mes_actual == "septiembre":
            if dia_actual <= 20:
                print("Estación: Verano")
            else:
                print("Estación: Otoño")
        elif mes_actual in ["octubre", "noviembre"]:
            print("Estación: Otoño")
        elif mes_actual == "diciembre":
            if dia_actual <= 20:
                print("Estación: Otoño")
            else:
                print("Estación: Invierno")
        else:
            print("Mes ingresado no reconocido")
    # ------------------- HEMISFERIO SUR -------------------
    elif zona == "sur":
        if mes_actual in ["enero", "febrero"]:
            print("Estación: Verano")
        elif mes_actual == "marzo":
            if dia_actual <= 20:
                print("Estación: Verano")
            else:
                print("Estación: Otoño")
        elif mes_actual in ["abril", "mayo"]:
            print("Estación: Otoño")
        elif mes_actual == "junio":
            if dia_actual <= 20:
                print("Estación: Otoño")
            else:
                print("Estación: Invierno")
        elif mes_actual in ["julio", "agosto"]:
            print("Estación: Invierno")
        elif mes_actual == "septiembre":
            if dia_actual <= 20:
                print("Estación: Invierno")
            else:
                print("Estación: Primavera")
        elif mes_actual in ["octubre", "noviembre"]:
            print("Estación: Primavera")
        elif mes_actual == "diciembre":
            if dia_actual <= 20:
                print("Estación: Primavera")
            else:
                print("Estación: Verano")
        else:
            print("Mes ingresado no reconocido")
    else:
        print("El hemisferio indicado no es válido")
