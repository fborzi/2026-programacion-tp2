"""Cuenta las palabras de una frase e informa la
longitud de cada una"""
cadena = input("Ingrese una frase: ")
cantidad_palabras = 0
palabra = ""

for letra in cadena:
    if letra != " ":
        palabra += letra
    elif palabra != "":
        cantidad_palabras += 1
        palabra = ""

if palabra != "":
    cantidad_palabras += 1
print("La cantidad de palabras en la cadena es:", cantidad_palabras)

palabra = ""

for letra in cadena:
    if letra != " ":
        palabra += letra
    elif palabra != "":
        print("La palabra", palabra, "tiene", len(palabra), "letra.")
        palabra = ""

if palabra != "":
    print("La palabra", palabra, "tiene", len(palabra), "letras.")
