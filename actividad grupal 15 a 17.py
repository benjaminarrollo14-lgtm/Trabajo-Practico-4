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

#         dias = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve",
#                 "diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete",
#                 "dieciocho", "diecinueve", "veinte", "veintiuno", "veintidós", "veintitrés",
#                 "veinticuatro", "veinticinco", "veintiséis", "veintisiete", "veintiocho",
#                 "veintinueve", "treinta", "treinta y uno"]

#         meses = ["", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
#                  "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

#         años = {
#             1970: "mil novecientos setenta",
#             1971: "mil novecientos setenta y uno",
#             1972: "mil novecientos setenta y dos",
#             1973: "mil novecientos setenta y tres",
#             1974: "mil novecientos setenta y cuatro",
#             1975: "mil novecientos setenta y cinco",
#             1976: "mil novecientos setenta y seis",
#             1977: "mil novecientos setenta y siete",
#             1978: "mil novecientos setenta y ocho",
#             1979: "mil novecientos setenta y nueve",
#             1980: "mil novecientos ochenta",
#             1981: "mil novecientos ochenta y uno",
#             1982: "mil novecientos ochenta y dos",
#             1983: "mil novecientos ochenta y tres",
#             1984: "mil novecientos ochenta y cuatro",
#             1985: "mil novecientos ochenta y cinco",
#             1986: "mil novecientos ochenta y seis",
#             1987: "mil novecientos ochenta y siete",
#             1988: "mil novecientos ochenta y ocho",
#             1989: "mil novecientos ochenta y nueve",
#             1990: "mil novecientos noventa",
#             1991: "mil novecientos noventa y uno",
#             1992: "mil novecientos noventa y dos",
#             1993: "mil novecientos noventa y tres",
#             1994: "mil novecientos noventa y cuatro",
#             1995: "mil novecientos noventa y cinco",
#             1996: "mil novecientos noventa y seis",
#             1997: "mil novecientos noventa y siete",
#             1998: "mil novecientos noventa y ocho",
#             1999: "mil novecientos noventa y nueve",
#             2000: "dos mil",
#             2001: "dos mil uno",
#             2002: "dos mil dos",
#             2003: "dos mil tres",
#             2004: "dos mil cuatro",
#             2005: "dos mil cinco",
#             2006: "dos mil seis",
#             2007: "dos mil siete",
#             2008: "dos mil ocho",
#             2009: "dos mil nueve",
#             2010: "dos mil diez",
#             2011: "dos mil once",
#             2012: "dos mil doce",
#             2013: "dos mil trece",
#             2014: "dos mil catorce",
#             2015: "dos mil quince",
#             2016: "dos mil dieciséis",
#             2017: "dos mil diecisiete",
#             2018: "dos mil dieciocho",
#             2019: "dos mil diecinueve",
#             2020: "dos mil veinte",
#             2021: "dos mil veintiuno",
#             2022: "dos mil veintidós",
#             2023: "dos mil veintitrés",
#             2024: "dos mil veinticuatro",
#             2025: "dos mil veinticinco",
#         }

#         dia, mes, año = map(int, fecha.split("/"))
#         return f"{dias[dia]} de {meses[mes]} de {años[año]}"


# class Principal:
#     def main():
#         fecha_ingresada = input("Ingrese una fecha (dd/mm/yyyy): ")
#         print("Fecha literal: ", FuncionesPrograma.getFechaString(fecha_ingresada))


# Principal.main()




