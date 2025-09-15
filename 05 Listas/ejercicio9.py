# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
# diferentes clientes:

lista_compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente usando append
lista_compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente
lista_compras[1][1] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente
lista_compras[0].remove("pan")

print(f"Lista final: {lista_compras}")
