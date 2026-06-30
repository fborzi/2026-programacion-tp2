cadena = input("Ingrese una cadena de texto: ")

cantidad_palabras = 0
palabra = ""
cantidad_letras = 0

cadena = cadena + " "

for caracter in cadena:

    if caracter != " ":
        palabra += caracter
        cantidad_letras += 1
    else:
        if cantidad_letras > 0:
            cantidad_palabras += 1
            print('La palabra "', palabra, '" tiene', cantidad_letras, 'letras.')
            palabra = ""
            cantidad_letras = 0
