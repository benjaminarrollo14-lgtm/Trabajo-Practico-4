#Trabajo practico 3
# actividad 1
# valorDecimal = float(input("Por favor, ingresa un número decimal: "))

# entero = int(valorDecimal)

# booleano = bool(valorDecimal)

# cadenaDeTexto = str(valorDecimal)

# print("Resultados de las conversiones")
# print(f"Valor original (float): {valorDecimal}")
# print(f"Convertido a entero (int): {entero}")
# print(f"Convertido a booleano (bool): {booleano}")
# print(f"Convertido a cadena de texto (str): {cadenaDeTexto}")

# print("Verificación de tipos de datos")
# print(f"Tipo de 'valorDecimal': {type(valorDecimal)}")
# print(f"Tipo de 'entero': {type(entero)}")
# print(f"Tipo de 'booleano': {type(booleano)}")
# print(f"Tipo de 'cadenaDeTexto': {type(cadenaDeTexto)}")

# actividad 2

# # Asignamos un número que sería un desbordamiento en otros lenguajes
# numero_grande = 123456789123456789123456789123456789

# # El tipo de dato sigue siendo 'int'
# print(f"El valor de la variable es: {numero_grande}")
# print(f"El tipo de la variable es: {type(numero_grande)}")

# # Python puede realizar operaciones con este número sin error
# resultado = numero_grande * 2
# print(f"\nEl resultado de la operación es: {resultado}")

# ejercicio 3


# numero_str = input("Por favor, ingresa un número de 3 dígitos (100-999): ")

# numero = int(numero_str)

# if 100 <= numero <= 999:
#     centenas = numero // 100

#     decenas = (numero % 100) // 10

#     unidades = numero % 10

#     suma = centenas + decenas + unidades

#     print(f"La suma de los dígitos de {numero} es: {suma}")

# else:
#     print("El número ingresado no es de 3 dígitos.")


# Ejercicio 4:

# print("Ejercicio 4: ")

# def calcular_cambio(cantidad):
#     billetes_monedas = [200, 100, 50, 20, 10, 5, 2, 1,
#                         0.50, 0.25, 0.10, 0.05]
#     resultado = {}

#     for valor in billetes_monedas:
#         cantidad_necesaria = int(cantidad // valor)
#         if cantidad_necesaria > 0:
#             resultado[valor] = cantidad_necesaria
#             cantidad = round(cantidad - cantidad_necesaria * valor, 2)

#     return resultado

# # Ejemplo:
# dinero = float(input("Ingrese la cantidad de dinero: "))
# cambio = calcular_cambio(dinero)

# print("Se necesitan: ")
# for valor, cantidad in cambio.items():
#     if valor >= 1:
#         print(f"{cantidad} billete(s) de {int(valor)}")
#     else:
#         print(f"{cantidad} moneda(s) de valor {valor:.2f}")

# # Ejercicio 5:

# print("Ejercicio 5: ")

# cadena_cinco = input("Ingrese una cadena (Palabra, frase): ")
# cadena_sin_espacios = cadena_cinco.replace(" ", "")
# print("Cadena sin espacios:", cadena_sin_espacios)

# # Ejercicio 6:

# print("Ejercicio 6: ")

# cadena_seis = "La lluvia en Mendoza es escasa"
# print("La cadena es:", cadena_seis)
# print("El numero de caracteres:", len(cadena_seis))

ejercicios 7,8 y 9( echo con el 6 del lauti
#  Ejercicio 7: Tamaño de cadena y contar vocales
# cadena = input("Ingrese una cadena: ")  
# tamanio = len(cadena)
# print("El tamaño de la cadena es:", tamanio)
# vocales = 0
# for letra in cadena.lower():
#     if letra in "aeiou":
#         vocales += 1
# print("La cadena tiene", vocales, "vocales")

# # Ejercicio 8 Reemplazar 'a' por 'e' 
# cadena = input("Ingrese una cadena: ")
# nueva_cadena = ""
# for letra in cadena:
#     if letra.lower() == "a":
#         nueva_cadena += "e"
#     else:
#         nueva_cadena += letra

# print("Cadena modificada:", nueva_cadena)

# # Ejercicio 9: Mostrar códigos ASCII de la cadena del Ejercicio 6
# codigos = ""
# for letra in cadena_seis:  
#     codigo = ord(letra)  #aca converti la cada caracter en codigo ASCII( tube que buscar como se hacia internet porque no supe como se hacia)
#     codigos += str(codigo) + " "  
# print("Códigos ASCII:", codigos.strip())  


#actividad 10
# cadena = input("Ingrese una cadena de texto: ")
# print("Ingrese si quiere Mayusculas o Minusculas")
# opcion = input("M para Mayusculas, m para Minusculas: ")
# if opcion == "M":
#     print(cadena.upper())  
# elif opcion == "m":
#     print(cadena.lower())

#actividad 11
# palabra = input("Ingrese una palabra: ")
# palabra2 = input("Ingrese otra palabra: ")
# if palabra == palabra2:
#     print("Las palabras son iguales")
# else:
#     print("Las palabras son diferentes")

#actividad 12
# cadena = "hipopótamo"
# extraer = cadena[3:5]
# print(extraer)

#actividad 13
# cadena1 = input("Ingrese la primera cadena de texto: ")
# cadena2 = input("Ingrese la segunda cadena de texto: ")
# if cadena2 in cadena1:
#     print("La segunda cadena se encuentra dentro de la primera.")
# else:
#     print("La segunda cadena no se encuentra dentro de la primera.")

#actividad 14
# En Python, no existe una distinción estricta entre variables de tipo valor y tipo referencia como en Java.
# Todas las variables en Python son referencias a objetos. Sin embargo, los tipos inmutables (como int, float, str, tuple) se comportan de manera similar a los tipos valor,
# mientras que los tipos mutables (como list, dict, set) se comportan como tipos referencia.

# 15- Indique que sucede si realizo la siguiente declaración de variable:
# x = None print(x)
# Explique y ejemplifique el uso de None

#Cuando en python se usa el "X= None" y lo usamos en un print esto hace que x tenga un valor nulo que no representa ni un numero, 
# ni un texto, si no que cuando usamos el print se imprime literalmente el "None"

#Un ejemplo de donde podemos usar el "None" seria en el caso de que una variable que queramos no retorne nada, por ejemplo en un if

# Numero = 25

# if Numero == 30:
#     Numero = None

# print(Numero)



# 16- Codifique un método que reciba como parámetro una cadena y determine si la
# misma contiene o no números.

# def numeros(cadena):
#     for caracter in cadena:
#         if caracter.isdigit():
#             return True
#     return False   


# texto = input("Ingrese una palabra: ")

# if numeros(texto):
#     print("La palabra que ingresaste contiene números")
# else:
#     print("La palabra que ingresaste no contiene números")


# 17- Cree una clase FuncionesPrograma y codifique una función estática getFechaString
# que reciba como parámetro una fecha y retorne la fecha como una cadena literal.
# Ejemplo recibo 15/10/1900, la salida debe ser
# Quince de Octubre de mil novecientos.
# Cree una clase Principal que contenga un método main y haga uso de la función
# getFechaString. 


# class FuncionesPrograma:

#     def getFechaString(fecha):

#           dias = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve",
#                 "diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete",
#                 "dieciocho", "diecinueve", "veinte", "veintiuno", "veintidós", "veintitrés",
#                 "veinticuatro", "veinticinco", "veintiséis", "veintisiete", "veintiocho",
#                 "veintinueve", "treinta", "treinta y uno"]
          
#           meses = ["", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
#                  "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
          


#           dia, mes, año = map(int, fecha.split("/"))
#           return f"{dias[dia]} de {meses[mes]} de {año}"
    

# class Principal:
#      def main(): 
#           fecha_ingresada = input("Ingrese una fecha (dd/mm/yyyy)")
#           print("Fecha literal: ", FuncionesPrograma.getFechaString(fecha_ingresada))



# Principal.main()

#Ejercicio18

# from datetime import date

# class FuncionesPrograma:
#     def getFechaDate(self, dia, mes, anio):
#         try:
#             return date(anio, mes, dia)
#         except ValueError as e:
#             return f"Fecha inválida: {e}"

# try:
#     dia = int(input("Ingrese el día: "))
#     mes = int(input("Ingrese el número de mes: "))
#     anio = int(input("Ingrese el año: "))

#     fp = FuncionesPrograma()
#     fecha = fp.getFechaDate(dia, mes, anio)
#     print("Fecha generada:", fecha)

# except ValueError:
#     print("Por favor, ingrese valores numéricos válidos.")

#     #Ejercicio19

# class OperacionMatematica:
#     def __init__(self, valor1, valor2):
#         self.valor1 = valor1
#         self.valor2 = valor2
#         self.operacion = None

#     def sumarNumeros(self):
#         return self.valor1 + self.valor2

#     def restarNumeros(self):
#         return self.valor1 - self.valor2

#     def multiplicarNumeros(self):
#         return self.valor1 * self.valor2

#     def dividirNumeros(self):
#         if self.valor2 != 0:
#             return self.valor1 / self.valor2
#         else:
#             return "Error: División por cero"

#     def aplicarOperacion(self, operacion):
#         self.operacion = operacion
#         if operacion == "+":
#             return self.sumarNumeros()
#         elif operacion == "-":
#             return self.restarNumeros()
#         elif operacion == "*":
#             return self.multiplicarNumeros()
#         elif operacion == "/":
#             return self.dividirNumeros()
#         else:
#             return "Operación no válida"


# class Calculo:
#     def main(self):
#         op = OperacionMatematica(10, 5)

#         print("Suma:", op.aplicarOperacion("+"))
#         print("Resta:", op.aplicarOperacion("-"))
#         print("Multiplicación:", op.aplicarOperacion("*"))
#         print("División:", op.aplicarOperacion("/"))

# if __name__ == "__main__":
#     calculo = Calculo()
#     calculo.main()

#     #Ejercicio20

# from math import gcd

# class Fraccion:
#     def __init__(self, numerador, denominador):
#         if denominador == 0:
#             raise ValueError("El denominador no puede ser cero.")
#         self.numerador = numerador
#         self.denominador = denominador
#         self.simplificar()

#     def simplificar(self):
#         comun = gcd(self.numerador, self.denominador)
#         self.numerador //= comun
#         self.denominador //= comun

#     def sumar(self, otra):
#         num = self.numerador * otra.denominador + otra.numerador * self.denominador
#         den = self.denominador * otra.denominador
#         return Fraccion(num, den)

#     def restar(self, otra):
#         num = self.numerador * otra.denominador - otra.numerador * self.denominador
#         den = self.denominador * otra.denominador
#         return Fraccion(num, den)

#     def multiplicar(self, otra):
#         num = self.numerador * otra.numerador
#         den = self.denominador * otra.denominador
#         return Fraccion(num, den)

#     def dividir(self, otra):
#         if otra.numerador == 0:
#             raise ValueError("No se puede dividir por una fracción con numerador cero.")
#         num = self.numerador * otra.denominador
#         den = self.denominador * otra.numerador
#         return Fraccion(num, den)

#     def __str__(self):
#         return f"{self.numerador}/{self.denominador}"

# class OperacionesFraccion:
#     def main(self):    
#         print("Ingrese los valores para dos fracciones:")
#         numerador1 = int(input("Numerador de la primera fracción: "))
#         denominador1 = int(input("Denominador de la primera fracción: "))
#         numerador2 = int(input("Numerador de la segunda fracción: "))
#         denominador2 = int(input("Denominador de la segunda fracción: "))

#         fraccion1 = Fraccion(numerador1, denominador1)
#         fraccion2 = Fraccion(numerador2, denominador2)

#         suma = fraccion1.sumar(fraccion2)
#         resta = fraccion1.restar(fraccion2)
#         producto = fraccion1.multiplicar(fraccion2)
#         division = fraccion1.dividir(fraccion2)

#         print("\nResultados:")
#         print("Suma:", suma)
#         print("Resta:", resta)
#         print("Multiplicación:", producto)
#         print("División:", division)


# operador = OperacionesFraccion()
# operador.main()
