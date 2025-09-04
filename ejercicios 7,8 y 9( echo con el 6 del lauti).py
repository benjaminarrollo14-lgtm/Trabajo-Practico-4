# Ejercicio 6: Mostrar cadena y su longitud
cadena_seis = "La lluvia en Mendoza es escasa"
print("La cadena es:", cadena_seis)
print("El numero de caracteres:", len(cadena_seis))

# Ejercicio 7: Tamaño de cadena y contar vocales
cadena = input("Ingrese una cadena: ")  
tamanio = len(cadena)
print("El tamaño de la cadena es:", tamanio)
vocales = 0
for letra in cadena.lower():
    if letra in "aeiou":
        vocales += 1
print("La cadena tiene", vocales, "vocales")

# Ejercicio 8 Reemplazar 'a' por 'e' 
cadena = input("Ingrese una cadena: ")
nueva_cadena = ""
for letra in cadena:
    if letra.lower() == "a":
        nueva_cadena += "e"
    else:
        nueva_cadena += letra

print("Cadena modificada:", nueva_cadena)

# Ejercicio 9: Mostrar códigos ASCII de la cadena del Ejercicio 6
codigos = ""
for letra in cadena_seis:  
    codigo = ord(letra)  #aca converti la cada caracter en codigo ASCII( tube que buscar como se hacia internet porque no supe como se hacia)
    codigos += str(codigo) + " "  
print("Códigos ASCII:", codigos.strip())  