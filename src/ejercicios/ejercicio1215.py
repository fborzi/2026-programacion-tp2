cadena = input("Ingrese una cadena:")

vocales = ""

for letras in cadena.lower():
    if letras in "aeiou" and letras not in vocales:
        vocales += letras

print("Las vocales que aparecen en la cadena son:", vocales)