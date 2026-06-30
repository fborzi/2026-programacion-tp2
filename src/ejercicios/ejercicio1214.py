cadena = input()

cantidad_palabras = 0
palabra_actual = ""
palabras = []

for caracter in cadena:
    if caracter == " ":
        if palabra_actual != "":
            palabras.append(palabra_actual)
            cantidad_palabras = cantidad_palabras + 1
            palabra_actual = ""
    else:
        palabra_actual = palabra_actual + caracter

if palabra_actual != "":
    palabras.append(palabra_actual)
    cantidad_palabras = cantidad_palabras + 1

print("La cantidad de palabras en la cadena es:", cantidad_palabras)

for palabra in palabras:
    print("La palabra '" + palabra + "' tiene", len(palabra), "letras.")