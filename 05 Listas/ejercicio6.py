# 6) Crear una lista con números del 10 al 30 (incluido), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros

lista_numeros = []

for n in range(10, 31, 5):
    lista_numeros.append(n)

print(f"""
Primer número: {lista_numeros[0]}
Segundo número: {lista_numeros[1]}
""")
