#Ejercicio20

from math import gcd

class Fraccion:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero.")
        self.numerador = numerador
        self.denominador = denominador
        self.simplificar()

    def simplificar(self):
        comun = gcd(self.numerador, self.denominador)
        self.numerador //= comun
        self.denominador //= comun

    def sumar(self, otra):
        num = self.numerador * otra.denominador + otra.numerador * self.denominador
        den = self.denominador * otra.denominador
        return Fraccion(num, den)

    def restar(self, otra):
        num = self.numerador * otra.denominador - otra.numerador * self.denominador
        den = self.denominador * otra.denominador
        return Fraccion(num, den)

    def multiplicar(self, otra):
        num = self.numerador * otra.numerador
        den = self.denominador * otra.denominador
        return Fraccion(num, den)

    def dividir(self, otra):
        if otra.numerador == 0:
            raise ValueError("No se puede dividir por una fracción con numerador cero.")
        num = self.numerador * otra.denominador
        den = self.denominador * otra.numerador
        return Fraccion(num, den)

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

class OperacionesFraccion:
    def main(self):    
        print("Ingrese los valores para dos fracciones:")
        numerador1 = int(input("Numerador de la primera fracción: "))
        denominador1 = int(input("Denominador de la primera fracción: "))
        numerador2 = int(input("Numerador de la segunda fracción: "))
        denominador2 = int(input("Denominador de la segunda fracción: "))

        fraccion1 = Fraccion(numerador1, denominador1)
        fraccion2 = Fraccion(numerador2, denominador2)

        suma = fraccion1.sumar(fraccion2)
        resta = fraccion1.restar(fraccion2)
        producto = fraccion1.multiplicar(fraccion2)
        division = fraccion1.dividir(fraccion2)

        print("\nResultados:")
        print("Suma:", suma)
        print("Resta:", resta)
        print("Multiplicación:", producto)
        print("División:", division)


operador = OperacionesFraccion()
operador.main()
