#Una matriz es simétrica si es igual a su transpuesta. Escribe un programa que verifique
# si una matriz es simétrica. - Leonel Fanchinelli
matriz = [[1, 2, 3],
          [2, 5, 6],
          [3, 6, 9]]

filas = len(matriz)
columnas = len(matriz[0])

if filas != columnas:
    print("La matriz no es cuadrada, por lo tanto no puede ser simétrica.")
else:
    simetrica = True
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] != matriz[j][i]:
                simetrica = False
                break  
        if not simetrica:
            break
    
    if simetrica:
        print("La matriz es simétrica.")
    else:
        print("La matriz NO es simétrica.")
