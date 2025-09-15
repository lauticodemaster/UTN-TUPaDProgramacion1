# 1) mostrar un saludo
print("Hola mundo")

# 2) pedir nombre y saludar
nombre = input("pone tu nombre: ")
print(f"Hola {nombre} que tal")

# 3) pedir datos y mostrarlos
nombre = input("nombre: ")
apellido = input("apellido: ")
edad = input("edad: ")
lugar = input("donde vivis: ")

print(f"Soy {nombre} {apellido} tengo {edad} años y vivo en {lugar}")

# 4) area y perimetro de un circulo
radio = float(input("radio del circulo: "))
area = 3.1416 * radio**2
perimetro = 2 * 3.1416 * radio

print("area:", area)
print("perimetro:", perimetro)

# 5) segundos a horas
seg = int(input("cantidad de segundos: "))
horas = seg // 3600
print(seg, "segundos son", horas, "hora/s")

# 6) tabla de multiplicar
n = int(input("numero para tabla: "))

for i in range(1,11):
    print(n, "x", i, "=", n*i)

# 7) operaciones basicas
a = int(input("primer numero distinto de 0: "))
b = int(input("segundo numero distinto de 0: "))

print("suma:", a+b)
print("resta:", a-b)
print("division:", a/b)
print("multiplicacion:", a*b)

# 8) indice de masa corporal
altura = float(input("altura en metros: "))
peso = float(input("peso en kg: "))

imc = peso / (altura**2)
print("tu imc es", imc)

# 9) celsius a fahrenheit
c = float(input("grados celsius: "))
f = (c * 9/5) + 32
print(c, "°C son", f, "°F")

# 10) promedio de 3 numeros
x = float(input("primer numero: "))
y = float(input("segundo numero: "))
z = float(input("tercer numero: "))

prom = (x+y+z)/3
print("el promedio es", prom)
