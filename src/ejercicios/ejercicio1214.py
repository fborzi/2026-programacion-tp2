texto = input("Ingrese una cadena de texto:")

palabra= ""
cantpalabras = 0

for caracter in texto:
    if caracter != " ":
        palabra += caracter
    else:
        if palabra != "":
            cantpalabra += 1
            print("La palabra ´" + palabra + "´ tiene", len(palabra), "letras.")
            palabra = ""

if palabra != "":
    cantpalabra += 1
    print("La palabra ´" + palabra + "´ tiene", len(palabra), "letras.")

print("La cantidad de palabras en la cadena es:", cantpalabras)