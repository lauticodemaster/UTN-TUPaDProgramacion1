# Escribe un programa que calcule la transpuesta de una matriz. La transpuesta de una 
# matriz intercambia sus filas por columnas - Leonel Fanchinelli

matriz = [[1, 2, 3],
          [4, 5, 6]]

transpuesta = []

for j in range(len(matriz[0])): 
    fila = []  
    for i in range(len(matriz)): 
        fila.append(matriz[i][j])  
    
    transpuesta.append(fila)

print("Matriz original:", matriz)
print("Matriz transpuesta:", transpuesta)
