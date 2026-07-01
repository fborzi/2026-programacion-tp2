"""Ejercicio 1215 - Vocales en una cadena"""

texto = input("Ingresá una cadena de caracteres: ")

vocales_encontradas = ""

for caracter in texto:
    caracter_min = caracter.lower()
    if caracter_min in "aeiouáéíóú":
        if caracter_min not in vocales_encontradas:
            if vocales_encontradas != "":
                vocales_encontradas += " "
            vocales_encontradas += caracter_min

print(f"Las vocales que aparecen en la cadena son: {vocales_encontradas}")