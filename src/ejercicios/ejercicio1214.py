""" Este programa solicita el ingreso de una cadena de texto y analiza su contenido
para determinar la cantidad de palabras que posee, así como la cantidad de
caracteres de cada una de ellas. La cadena puede contener espacios al inicio
y al final, y las palabras se encuentran separadas por espacios en blanco,
realizando el análisis sin utilizar la función split()."""

texto = input("Ingrese una cadena de texto: ")

palabra_actual = ""
cantidad_palabras = 0
lista_palabras = []

for c in texto:
    if c != " ":
        palabra_actual += c
    else:
        if palabra_actual != "":
            cantidad_palabras += 1
            lista_palabras.append((palabra_actual, len(palabra_actual)))
            palabra_actual = ""

if palabra_actual != "":
    cantidad_palabras += 1
    lista_palabras.append((palabra_actual, len(palabra_actual)))

print(f"La cantidad de palabras en la cadena es: {cantidad_palabras}")

for palabra, largo in lista_palabras:
    print(f"La palabra '{palabra}' tiene {largo} letras.")