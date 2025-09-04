#Ejercicio18

from datetime import date

class FuncionesPrograma:
    def getFechaDate(self, dia, mes, anio):
        try:
            return date(anio, mes, dia)
        except ValueError as e:
            return f"Fecha inválida: {e}"

try:
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el número de mes: "))
    anio = int(input("Ingrese el año: "))

    fp = FuncionesPrograma()
    fecha = fp.getFechaDate(dia, mes, anio)
    print("Fecha generada:", fecha)

except ValueError:
    print("Por favor, ingrese valores numéricos válidos.")
