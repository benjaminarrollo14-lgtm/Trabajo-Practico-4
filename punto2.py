# Asignamos un número que sería un desbordamiento en otros lenguajes
numero_grande = 123456789123456789123456789123456789

# El tipo de dato sigue siendo 'int'
print(f"El valor de la variable es: {numero_grande}")
print(f"El tipo de la variable es: {type(numero_grande)}")

# Python puede realizar operaciones con este número sin error
resultado = numero_grande * 2
print(f"\nEl resultado de la operación es: {resultado}")