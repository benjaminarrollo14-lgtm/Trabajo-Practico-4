valorDecimal = float(input("Por favor, ingresa un número decimal: "))

entero = int(valorDecimal)

booleano = bool(valorDecimal)

cadenaDeTexto = str(valorDecimal)

print("Resultados de las conversiones")
print(f"Valor original (float): {valorDecimal}")
print(f"Convertido a entero (int): {entero}")
print(f"Convertido a booleano (bool): {booleano}")
print(f"Convertido a cadena de texto (str): {cadenaDeTexto}")

print("Verificación de tipos de datos")
print(f"Tipo de 'valorDecimal': {type(valorDecimal)}")
print(f"Tipo de 'entero': {type(entero)}")
print(f"Tipo de 'booleano': {type(booleano)}")
print(f"Tipo de 'cadenaDeTexto': {type(cadenaDeTexto)}")