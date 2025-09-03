# Ejercicio 4:

print("Ejercicio 4: ")

def calcular_cambio(cantidad):
    billetes_monedas = [200, 100, 50, 20, 10, 5, 2, 1,
                        0.50, 0.25, 0.10, 0.05]
    resultado = {}

    for valor in billetes_monedas:
        cantidad_necesaria = int(cantidad // valor)
        if cantidad_necesaria > 0:
            resultado[valor] = cantidad_necesaria
            cantidad = round(cantidad - cantidad_necesaria * valor, 2)

    return resultado

# Ejemplo:
dinero = float(input("Ingrese la cantidad de dinero: "))
cambio = calcular_cambio(dinero)

print("Se necesitan: ")
for valor, cantidad in cambio.items():
    if valor >= 1:
        print(f"{cantidad} billete(s) de {int(valor)}")
    else:
        print(f"{cantidad} moneda(s) de valor {valor:.2f}")

# Ejercicio 5:

print("Ejercicio 5: ")

cadena_cinco = input("Ingrese una cadena (Palabra, frase): ")
cadena_sin_espacios = cadena_cinco.replace(" ", "")
print("Cadena sin espacios:", cadena_sin_espacios)

# Ejercicio 6:

print("Ejercicio 6: ")

cadena_seis = "La lluvia en Mendoza es escasa"
print("La cadena es:", cadena_seis)
print("El numero de caracteres:", len(cadena_seis))