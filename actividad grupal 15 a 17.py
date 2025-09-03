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

