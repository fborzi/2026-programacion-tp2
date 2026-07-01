"""Ejercicio 1219 - Imprimir palabras de una frase"""

frase = input("Ingresá una frase: ")

palabra_actual = ""

for caracter in frase:
    if caracter != " ":
        palabra_actual += caracter
    else:
        print(palabra_actual)
        palabra_actual = ""

print(palabra_actual)