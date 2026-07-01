"""
 ejercicio 1214,el programa informa la cantidad de palabras de una cadena
y la cantidad de letras que tiene cada una, sin usar split().
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
            print("La palabra", "'" + palabra + "'", "tiene", len(palabra), "letras.")
            palabra = ""

if palabra != "":
    cantidad_palabras += 1
    print("La palabra", "'" + palabra + "'", "tiene", len(palabra), "letras.")

print("La cantidad de palabras en la cadena es:", cantidad_palabras)
