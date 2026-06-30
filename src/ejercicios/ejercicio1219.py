cadena = input()
palabra_actual = ""

for caracter in cadena:
    if caracter == " ":
        if palabra_actual != "":
            print(palabra_actual)
            palabra_actual = ""
    else:
        palabra_actual = palabra_actual + caracter

if palabra_actual != "":
    print(palabra_actual)