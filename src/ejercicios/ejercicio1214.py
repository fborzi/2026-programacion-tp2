cadena = input("Ingrese una cadena de texto: ")
palabras = []
palabra_actual = ""
for caracter in cadena:
    if caracter != " ":   
        palabra_actual += caracter
    else:
        if palabra_actual != "":   
            palabras.append(palabra_actual)
            palabra_actual = ""

if palabra_actual != "":
    palabras.append(palabra_actual)

print("La cantidad de palabras en la cadena es:", len(palabras))
for palabra in palabras:
    print("La palabra '", palabra, "' tiene", len(palabra), "letras.")
