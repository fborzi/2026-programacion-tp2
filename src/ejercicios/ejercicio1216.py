cadena = input()
cadena = cadena.lower()
vocales_encontradas = ""

for caracter in cadena:
    if caracter in "aeiou" and caracter not in vocales_encontradas:
        vocales_encontradas = vocales_encontradas + caracter

print("Las vocales que aparecen en la cadena son:", vocales_encontradas)