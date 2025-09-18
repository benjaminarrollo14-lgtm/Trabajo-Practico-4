# Ejercicio 9: Mostrar códigos ASCII de la cadena del Ejercicio 6
codigos = ""
for letra in cadena_seis:  # Usamos la cadena del Ejercicio 6
    codigo = ord(letra)  # Convertimos cada carácter a su código ASCII
    codigos += str(codigo) + " "  # Agregamos el código y un espacio
print("Códigos ASCII:", codigos.strip())  # Mostramos los códigos sin el espacio final