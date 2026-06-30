"escribi un programa que pide al usuario una cadena de texto y luego muestra las vocales que aparecen en ella, sin repetirlas."

print("")
cadena = input("")

vocales_encontradas = ""

for char in cadena:
    if char.lower() in "aeiou" and char.lower() not in vocales_encontradas:
        vocales_encontradas += char.lower()

print("Las vocales que aparecen en la cadena son: " + vocales_encontradas)
