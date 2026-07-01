"""
Busca vocales sin repetir (sin usar listas), respetando el orden de aparición.
"""
cadena = input("Ingrese una cadena de caracteres:")
vocales_encontradas = ""

for caracter in cadena.lower():
    if caracter in "aeiou" and caracter not in vocales_encontradas:
        vocales_encontradas += caracter

if vocales_encontradas == "":
    print("La cadena no contiene vocales.")
else:
    resultado = ""
    for i in range(len(vocales_encontradas)):
        if i > 0:
            resultado += " "
        resultado += vocales_encontradas[i]
    print(f"Las vocales que aparecen en la cadena son: {resultado}")