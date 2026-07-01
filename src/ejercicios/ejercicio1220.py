"""
El programa encripta un texto utilizando la cifra del César,las letras se corren la cantidad de posiciones indicada por el usuario
los caracteres que no son letras se dejan igual.
"""

abecedario = "abcdefghijklmnñopqrstuvwxyz"

texto = input("Ingrese un texto: ")
corrimiento = int(input("Ingrese el corrimiento: "))

texto_encriptado = ""

for letra in texto:
    if letra in abecedario:
        posicion = abecedario.index(letra)
        nueva_posicion = (posicion + corrimiento) % 27
        texto_encriptado += abecedario[nueva_posicion]
    else:
        texto_encriptado += letra

print(texto_encriptado)
