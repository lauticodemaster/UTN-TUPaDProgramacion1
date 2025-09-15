# =========================
# Archivo de ejercicios - Rama de GitHub
# Cada sección corresponde a un integrante del grupo
# =========================

# 1. Maximiliano Mendez
# ---------------------------------
#CASTEO: Codifique un programa que solicite el ingreso de un número decimal y 
#asigne el mismo a una variable valorDecimal, aplique las operaciones de CASTING para 
#convertir la variable en otro tipo de dato. Investigue las diferentes formas de lograr la 
#--conversión. Muestre por pantalla el resultado de las conversiones.  
valorDecimal = int(input("Ingrese un numero decimal: ")) #decimal
print(valorDecimal, type(valorDecimal)) 
valorString = str(valorDecimal)#string
print(valorString, type(valorString))
valorBool = bool(valorDecimal)#bool
print(valorBool, type(valorBool))
valorFloat = float(valorDecimal)#float
print(valorFloat, type(valorFloat))
# ---------------------------------


# 2. Mailén Ortiz
# ---------------------------------

# Si se asigna un valor a una variable fuera del rango permitido y el programa no tiene ninguna verificación, el código va a seguir ejecutándose normalmente pero va a generarse un error lógico, aunque no aparezca un mensaje específico de error cuando lo ejecutemos en la terminal. Para evitarlo, se debe validar el valor usando condicionales que, en el caso que sea un valor fuera de rango, muestre un mensaje de error y vuelva a pedir el dato hasta que esté dentro del rango correcto.

#Ejemplo: Si en un bucle se ingresa un valor fuera del rango estipulado este va a generar un mensaje de error y va a pedirle al usuario volver a ingresar un número dentro del rango.

nota = -3 #Se le da un valor fuera de rango para que entre al bucle While 

while (nota < 1) or (nota > 10):
    nota = int(input("Ingrese una nota en el rango del 1 al 10:")) #Se ingresa una nueva nota

    if (nota >= 1) and (nota <= 10): #Verifica si está en el rango, si no lo está vuelve a ejecutarse el bucle.
        print("Nota ingresada correctamente")
    else:
        print(f"La nota ingresada: {nota}, no es válida. Ingrese una nota en el rango del 1 al 10")

# ---------------------------------


# 3. Nicolás Ibañez
# ---------------------------------
# Algoritmo para sumar los 3 dígitos de un número de 3 cifras

# 1. Creamos la entrada de los datos 
numero = int(input("Ingrese un número de 3 dígitos (100 - 999): "))

# 2. sacamos los digitos de dígitos usando módulo y división entera
digito3 = numero % 10          # Último dígito
numero = numero // 10          # Quita el último dígito

digito2 = numero % 10          # Segundo dígito
numero = numero // 10          # Quita el segundo dígito

digito1 = numero % 10          # Primer dígito

# 3. Suma de los dígitos
suma = digito1 + digito2 + digito3

# 4. Salida
print("La suma de los dígitos es:", suma)

# ---------------------------------


# 4. Lautaro Fernández
# ---------------------------------
 #Programa que ayuda a la cajera a calcular cuántos billetes y monedas se necesitan
monto = float(input("Ingrese una cantidad de dinero: "))

billetes = [200, 100, 50, 20, 10, 5, 2, 1]
monedas = [0.50, 0.25, 0.10]

print("Cantidad ingresada:", monto)

for b in billetes:
    cantidad = int(monto // b)
    if cantidad > 0:
        print(cantidad, "billete(s) de", b)
    monto = round(monto - cantidad * b, 2)

for m in monedas:
    cantidad = int(monto // m)
    if cantidad > 0:
        print(cantidad, "moneda(s) de", m)
    monto = round(monto - cantidad * m, 2)
# ---------------------------------


# 5. Maximiliano Reinoso
# ---------------------------------
#En este programa se pide que el usuario ingrese una oracion
oracion = input("Ingrese una oración: ")
#La oracion sera mostrada en pantalla
print (oracion.replace(" ",""))
# ---------------------------------


# 6. Leonel Fanchinelli
# ---------------------------------

# solicito el texto
texto = "La lluvia en Mendoza es escasa"

# obtengo el tamanño
tamano = len(texto)

# muestro el resultado
print("El tamaño de la cadena es:", tamano)
# ---------------------------------


# 7. Leonel Fachienlli
# ---------------------------------
# pido la cadena al usuario
cadena = input("Ingrese una cadena de texto: ")

# calculo el tamaño de la cadena
tamano = len(cadena)

# cuento las vocales
contador_vocales = 0
for caracter in cadena.lower():   # .lower() convierte todo a minúsculas
    if caracter in "aeiou":
        contador_vocales += 1

# muestro los resultados
print("El tamaño de la cadena es:", tamano)
print("La cantidad de vocales es:", contador_vocales)
# ---------------------------------


# 8. Mailén Ortiz
# ---------------------------------

frase = input("Ingrese una frase: ")
nuevaPalabra = "" #Variable vacía donde se almacenará la nueva palabra

for letra in frase: #Recorre cada letra de la frase
    if letra.lower() == "a": #En el caso de ser mayúscula la transforma en minúscula.
        nuevaPalabra += "e" #Remplaza la "a" por una "e"
    else:
        nuevaPalabra += letra #Si no la deja igual 

print(nuevaPalabra) 

# ---------------------------------


# 9. Nicolás Ibañez
# ---------------------------------
# cadena = "La lluvia en Mendoza es escasa"

# Definimos la cadena del ejercicio 6 
cadena = "La lluvia en Mendoza es escasa"

# Hacemos q el for lea toda la cadena letra por letra
for caracter in cadena:
    # La función ord() lo vuelve al  carácter en su valor ASCII
    # Con end=" " hacemos que se impriman en una sola línea separados por espacios y se lea mas facil
    print(ord(caracter), end=" ")


# ---------------------------------


# 10. Maximiliano Reinoso
# ---------------------------------
#El usuario ingresa una oracion
oracion = input("Ingrese una oración: ")
print("Elija a que quiere convertir el texto")
#Elije como quiere mostrarse en pantalla entre mayuscula y minuscula con la variable "Opcion"
opcion = int(input("1)Mayusculas 2)Minusculas: "))
#Usando if hacemos que la opcion correcta se active e imprima segun desea el usuario
if opcion == 1:
    print(oracion.upper())
elif opcion ==2:
    print(oracion.lower())
else:
    print("Elija un numero entre las opciones")# ---------------------------------


# 11. Lautaro Fernández
# ---------------------------------
# El programa pide dos palabras por teclado. Luego compara si son iguales usando ==.
# Si coinciden, imprime un mensaje de igualdad, si no, avisa que son distintas.
palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")

if palabra1 == palabra2:
    print("Las palabras son iguales")
else:
    print("Las palabras son distintas")
# ---------------------------------


# 12. Leonel Fanchinelli
# ---------------------------------
cadena = "hipopotamo"

# extraigo cuarta y quinta letra 
cuarta = cadena[3]
quinta = cadena[4]
#escribo las letras extraidas de la palabra 
print("Cuarta letra:", cuarta)
print("Quinta letra:", quinta)
# ---------------------------------


# 13. Maximiliano Mendez
# ---------------------------------
#Pedir el ingreso de dos cadenas por por teclado, indicar si la segunda cadena se 
#encuentra dentro de la primera.  
cadena1 = input("Ingrese la primera Cadena: ").upper()
cadena2 = input("Ingrese la Segunda Cadena: ").upper()
#Le preguntamos a la maquina si encuentra la cadena 2 en la 1
if cadena1.find(cadena2) == -1:
    print("La segunda cadena NO se encontro en la primera")
else:
    print("La segunda cadena se encontro en la primera")

# ---------------------------------


# 14. Mailén Ortiz
# ---------------------------------

# En Python no hay variables de tipo valor como en Java. Todo en Python es un objeto y las variables apuntan a ese objeto en memoria. Si el objeto es inmutable (como números, strings o tuplas), cambiar otra variable que apunte al mismo objeto no lo afectae. Si el objeto es mutable (como listas o diccionarios), cualquier cambio desde una variable afecta a las demás que apuntan al mismo objeto.

# ---------------------------------


# 15. Maximiliano
# ---------------------------------
x = None 
print(x)
#Al ejecutar imprime "None"
#None es un "valor" que se le asigna a una variable, este valor esta vacio, no tiene nada y por ende si ejecutamos en vez de dar 0 dice none
#Sirve para inicializar variables antes de asignarle un valor real como en el ejemplo a comtinuacion

#Inicializo variable
num = None

#Ingreso valor
num = int(input("Ingrese su edad: "))

#Muestro numero
print(num)# ---------------------------------


# 16. Lautaro Fernández
# ---------------------------------
# Verificar si una cadena contiene números

texto = input("Ingrese una cadena: ")

tiene_numero = False
for caracter in texto:
    if caracter.isdigit():
        tiene_numero = True

if tiene_numero:
    print("La cadena contiene números")
else:
    print("La cadena NO contiene números")

# ---------------------------------


# 17/18 Luciano Nicolas Ibañez
# ---------------------------------
from datetime import date

class FuncionesPrograma:

    @staticmethod
    def getFechaString(fecha: date) -> str:
        # Ponemos el nombre de cada numero en formato cadena
        dias = {
            1: "Uno", 2: "Dos", 3: "Tres", 4: "Cuatro", 5: "Cinco",
            6: "Seis", 7: "Siete", 8: "Ocho", 9: "Nueve", 10: "Diez",
            11: "Once", 12: "Doce", 13: "Trece", 14: "Catorce", 15: "Quince",
            16: "Dieciséis", 17: "Diecisiete", 18: "Dieciocho", 19: "Diecinueve", 20: "Veinte",
            21: "Veintiuno", 22: "Veintidós", 23: "Veintitrés", 24: "Veinticuatro", 25: "Veinticinco",
            26: "Veintiséis", 27: "Veintisiete", 28: "Veintiocho", 29: "Veintinueve", 30: "Treinta",
            31: "Treinta y uno"
        }

        # Anotamos los meses pa
        meses = {
            1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio",
            7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
        }

        # Anotamos algunos años comunes(podemos todos pero nos quedamos aca hasta el año q viene)
        anios = {
            1900: "mil novecientos",
            1910: "mil novecientos diez",
            1920: "mil novecientos veinte",
            1930: "mil novecientos treinta",
            1940: "mil novecientos cuarenta",
            1950: "mil novecientos cincuenta",
            1960: "mil novecientos sesenta",
            1970: "mil novecientos setenta",
            1980: "mil novecientos ochenta",
            1990: "mil novecientos noventa",
            2000: "dos mil",
            2010: "dos mil diez",
            2020: "dos mil veinte",
            2024: "dos mil veinticuatro"
        }

        # Las convertimos para q sea parte de la fecha y de un retorno mejor
        dia_str = dias[fecha.day]
        mes_str = meses[fecha.month]
        anio_str = anios[fecha.year]

        return f"{dia_str} de {mes_str} de {anio_str}"

    @staticmethod #Método que se usa para que la función solo realice una tarea y no modifique ni use datos externos de la clase o instancia
    def getFechaDate(dia: int, mes: int, anio: int) -> date:
        return date(anio, mes, dia)

#Todo lo q es la rama principal donde va a retornar todo tanto la fecha como cadena y los datos q pide el usuario
class Principal:
    @staticmethod
    def main():
        # Pedir fecha al usuario
        dia = int(input("Ingrese el día: "))
        mes = int(input("Ingrese el mes: "))
        anio = int(input("Ingrese el año: "))

        # Crear fecha y mostrar en cadena
        fecha = FuncionesPrograma.getFechaDate(dia, mes, anio)
        print("Tu fecha convertida:", FuncionesPrograma.getFechaString(fecha))


if __name__ == "__main__":
    Principal.main()



# ---------------------------------


# 19. Maximiliano Mendez
# ---------------------------------
# #cree una clase OperacionMatematica con dos atributos valor1 y valor2 y un #atributo de nombre operación. 
#Agregue a la clase los siguientes 5 métodos e implemente la lógica correspondiente:  
#sumarNumeros() 
#restarNumeros() 
#multiplicarNumeros() 
#dividirNumeros() 
#El quinto método será el siguiente:  
#aplicarOperacion(operacion){  
#…………………..  
#}  
#Cree una clase Calculo que contenga un método main, donde cree una instancia de la 
#clase OperacionMatematica, asigne 2 valores para las variables de la instancia y 
#ejecute la función aplicarOperacion, pasando como parámetro primero “+”, después “
#”, a continuación “*” y finalmente “/”. Muestre por pantalla el resultado de las 
#operaciones.  
class OperacionMatematica:
    #hacemos la clase para realizar operaciones matematicas
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    def sumarNumeros(self):
        return self.valor1 + self.valor2

    def restarNumeros(self):
        return self.valor1 - self.valor2

    def multiplicarNumeros(self):
        return self.valor1 * self.valor2

    def dividirNumeros(self):
        if self.valor2 == 0:
            return "Error: No se puede dividir por cero."
        return self.valor1 / self.valor2

    def aplicarOperacion(self, operacion):
        #Esto aplica una operación matemática basada en los símbolo correspondientes.
        #Parámetros:
        #Los simbolos en forma string de la operación ('+', '-', '*', '/').
        operaciones = {
            '+': self.sumarNumeros,
            '-': self.restarNumeros,
            '*': self.multiplicarNumeros,
            '/': self.dividirNumeros,
        }
        
        if operacion in operaciones:
            return operaciones[operacion]()
        else:
            return "Error: Operación no válida."

# Inicio del programa 
if __name__ == "__main__":
    # Creamos una instancia de OperacionMatematica con los valores 10 y 24
    operacion = OperacionMatematica(10, 24)

    # Definimos una lista con los símbolos de las operaciones a realizar
    simbolos_operaciones = ['+', '-', '*', '/']

    # Iteramos sobre la lista para aplicar cada operación
    for simbolo in simbolos_operaciones:
        resultado = operacion.aplicarOperacion(simbolo)
        print(f"El resultado de la operación '{simbolo}' es: {resultado}")
# ---------------------------------


# 20. Maximiliano Reinoso
# ---------------------------------
#Fracción
class fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
#armamos las operaciones suma, resta, multiplicacion y division
    def __str__(self):
        return f"{self.numerador}/{self.denominador}"
    
    def sumar(self, f2):
        num= self.numerador * f2.denominador + f2.numerador * self.denominador
        den= self.denominador * f2.denominador
        return fraccion(num, den)
    
    def resta(self, f2):
        num= self.numerador * f2.denominador - f2.numerador * self.denominador
        den= self.denominador * f2.denominador
        return fraccion(num, den)
    
    def multiplicar(self, f2):
        num= self.numerador * f2.numerador
        den = self.denominador * f2.denominador
        return fraccion(num, den)
    
    def dividir(self, f2):
        num= self.numerador * f2.denominador
        den= self. denominador * f2.numerador
        return fraccion(num, den)
    
#Codigo principal

#el usuario ingresa el valor de ambas fracciones
#fraccion 1
num1 = int(input("Ingrese el numerador de la primera fracción: "))
den1 = int(input("Ingrese el denominador de la primera fracción: "))
#fraccion 2
num2 = int(input("Ingrese el numerador de la segunda fracción: "))
den2 = int(input("Ingrese el denominador de la segunda fracción: "))
#agarramos los valores de numerador y denominador y armamos ambas fracciones
f1 = fraccion(num1, den1)
f2 = fraccion(num2, den2)

#Llamamos la funcion Fraccion para hacer las operaciones correspondientes
suma= f1.sumar(f2)
resta= f1.resta(f2)
multiplicacion= f1.multiplicar(f2)
division= f1.dividir(f2)

#Mostramos por pantalla los resultados
print(f"La suma de ambas fracciones es: {suma}")
print(f"La resta de ambas fracciones es: {resta}")
print(f"La multiplicacion de ambas fracciones es: {multiplicacion}")
print(f"La division de ambas fracciones es: {division}")# ---------------------------------
