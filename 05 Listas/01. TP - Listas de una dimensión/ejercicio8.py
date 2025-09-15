# Escribe un programa que identifique y muestre los elementos que se repiten en una 
# lista - Maximiliano Mendez

# Le pide al usuario una lista de elementos separados por espacio
elementos = input("Ingrese una lista de elementos separados por espacio: ")
# Esto convierte la lista en los elementos que podemos guardar (puede tener números o strings)
lista = elementos.split()
# Lista para guardar los repetidos
repetidos = []
# Revisamos la lista y miramos si hay repetidos
for elementos in lista:
    if lista.count(elementos) > 1 and elementos not in repetidos:
        # Evita guardar elementos Duplicados
        repetidos.append(elementos)  
# Mostramos resultados
if repetidos:
    print("Elementos repetidos en la lista:", repetidos)
else:
    print("No hay elementos repetidos.")
