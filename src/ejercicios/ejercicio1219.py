"""
El programa recibe una frase e imprime cada palabra
en una línea distinta, sin utilizar split().
"""

frase = input("Ingrese una frase: ")

palabra = ""

for letra in frase:
    if letra != " ":
        palabra += letra
    else:
        print(palabra)
        palabra = ""

print(palabra)
