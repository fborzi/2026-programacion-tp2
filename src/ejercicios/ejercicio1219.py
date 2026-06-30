"""Este programa solicita el ingreso de una frase y muestra cada una de
las palabras que la componen en líneas separadas. Se considera que
las palabras están separadas por espacios en blanco y que la frase no
contiene espacios al inicio ni al final, realizando el procesamiento sin
utilizar la función split()."""

frase = input("Ingrese una frase: ")

palabra = ""

for c in frase:
    if c != " ":
        palabra += c
    else:
        print(palabra)
        palabra = ""

print(palabra)
