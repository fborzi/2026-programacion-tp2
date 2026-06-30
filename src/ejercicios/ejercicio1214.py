cadena = input("Ingrese una frase: ")

cantidadPalabras = 0
cantidadLetras = 0
palabra = ""

for letra in cadena:

    if letra != " ":
        palabra += letra
        cantidadLetras += 1

    else:
        if palabra != "":
            cantidadPalabras += 1
            print("La palabra", palabra, "tiene", cantidadLetras, "letras.")
            palabra = ""
            cantidadLetras = 0

# Procesar la última palabra
if palabra != "":
    cantidadPalabras += 1
    print("La palabra", palabra, "tiene", cantidadLetras, "letras.")

print("La cantidad de palabras en la cadena es:", cantidadPalabras)