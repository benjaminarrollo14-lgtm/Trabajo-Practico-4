#Ejercicio19

class OperacionMatematica:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2
        self.operacion = None

    def sumarNumeros(self):
        return self.valor1 + self.valor2

    def restarNumeros(self):
        return self.valor1 - self.valor2

    def multiplicarNumeros(self):
        return self.valor1 * self.valor2

    def dividirNumeros(self):
        if self.valor2 != 0:
            return self.valor1 / self.valor2
        else:
            return "Error: División por cero"

    def aplicarOperacion(self, operacion):
        self.operacion = operacion
        if operacion == "+":
            return self.sumarNumeros()
        elif operacion == "-":
            return self.restarNumeros()
        elif operacion == "*":
            return self.multiplicarNumeros()
        elif operacion == "/":
            return self.dividirNumeros()
        else:
            return "Operación no válida"


class Calculo:
    def main(self):
        op = OperacionMatematica(10, 5)

        print("Suma:", op.aplicarOperacion("+"))
        print("Resta:", op.aplicarOperacion("-"))
        print("Multiplicación:", op.aplicarOperacion("*"))
        print("División:", op.aplicarOperacion("/"))

if __name__ == "__main__":
    calculo = Calculo()
    calculo.main()
