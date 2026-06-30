"escribi un programa que pide al usuario que ingrese una cadena de texto y luego cuente la cantidad de palabras en la cadena. El programa tambien imprime cada palabra junto con su longitud."

print("Ingrese una cadena de texto:")
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

print(f"La cantidad de palabras en la cadena es: {len(palabras)}")

for palabra in palabras:
    print(f"La palabra '{palabra}' tiene {len(palabra)} letras.")
