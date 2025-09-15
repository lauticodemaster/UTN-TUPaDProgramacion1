#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

print("Clasificación de un terremoto según la escala de Richter:")

valor = float(input("Ingrese la magnitud del sismo: "))

if valor < 0:
    print("Magnitud inválida")
elif valor < 3:
    print("Muy leve (imperceptible)")
elif 3 <= valor < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= valor < 5:
    print("Moderado (sentido por personas, sin daños graves)")
elif 5 <= valor < 6:
    print("Fuerte (puede afectar estructuras débiles)")
elif 6 <= valor < 7:
    print("Muy fuerte (daños significativos posibles)")
elif valor >= 7:
    print("Extremo (graves daños a gran escala posibles)")
