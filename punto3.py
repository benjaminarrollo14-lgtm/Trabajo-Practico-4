
numero_str = input("Por favor, ingresa un número de 3 dígitos (100-999): ")

numero = int(numero_str)

if 100 <= numero <= 999:
    centenas = numero // 100

    decenas = (numero % 100) // 10

    unidades = numero % 10

    suma = centenas + decenas + unidades

    print(f"La suma de los dígitos de {numero} es: {suma}")

else:
    print("El número ingresado no es de 3 dígitos.")