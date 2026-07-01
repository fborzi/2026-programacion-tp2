"""Ejercicio 1216 - Reemplazar carácter"""

frase = input("Ingresá una frase: ")
caracter_a_buscar = input("Ingresá un carácter a reemplazar (longitud 1): ")

frase_modificada = ""

for caracter in frase:
    if caracter == caracter_a_buscar:
        frase_modificada += "*"
    else:
        frase_modificada += caracter

print(frase_modificada)