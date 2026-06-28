"""
En este ejercicio se pide que se ingrese una cadena de texto.
Luego buscamos la cantidad de palabras que tiene la cadena,
la cantidad de caracteres y el resultado se imprime en pantalla.
"""
cadena = input("Ingrese una cadena: ")

cantidad_palabras = 0
palabra = ""

for letra in cadena:
    if letra != " ":
        palabra += letra
    else:
        if palabra != "":
            cantidad_palabras += 1
            print("La palabra '" + palabra + "' tiene", len(palabra), "letras.")
            palabra = ""

if palabra != "":
    cantidad_palabras += 1
    print("La palabra '" + palabra + "' tiene", len(palabra), "letras.")

print("La cantidad de palabras en la cadena es:", cantidad_palabras)
