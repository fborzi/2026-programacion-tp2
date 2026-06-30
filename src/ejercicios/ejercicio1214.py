"escribi un programa que pide al usuario que ingrese una cadena de texto y luego cuente la cantidad de palabras en la cadena. El programa tambien imprime cada palabra junto con su longitud."

cadena = input("")
palabras = []
palabra_actual = ""

for char in cadena:
    if char != " ":
        palabra_actual += char
    else:
        if palabra_actual != "":
            palabras.append(palabra_actual)
            palabra_actual = ""


if palabra_actual != "":
    palabras.append(palabra_actual)

print("La cantidad de palabras en la cadena es: " + str(len(palabras)))

for palabra in palabras:
    print("La palabra '" + palabra + "' tiene " + str(len(palabra)) + " letras.")
