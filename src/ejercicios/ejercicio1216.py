"escribi un programa que pide al usuario una frase y un caracter, y luego reemplaza todas las apariciones de ese caracter en la frase con un asterisco (*). El programa quita las mayúsculas y minúsculas."

frase = input("frase: ")
caracter = input("caracter: ")

resultado = ""

for char in frase:
    if char.lower() == caracter.lower():
        resultado += "*"
    else:
        resultado += char

print(f"La frase modificada es: {resultado}")
