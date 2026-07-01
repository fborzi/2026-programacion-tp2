"""
Arma cada cadena a mano (sin split()) y muestra cantidad de palabras y letras de cada una.
"""
cadena = input("Ingrese la cadena:")

palabra_actual = ""
palabras = []

for caracter in cadena:
    if caracter == " ":
        if palabra_actual != "":
            palabras.append(palabra_actual)
            palabra_actual = ""
    else:
        palabra_actual += caracter

if palabra_actual != "":
    palabras.append(palabra_actual)

print(f"La cantidad de palabras en la cadena es: {len(palabras)}")
for palabra in palabras:
    print(f"La palabra '{palabra}' tiene {len(palabra)} letras.")