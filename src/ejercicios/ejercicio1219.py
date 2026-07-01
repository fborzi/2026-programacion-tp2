"""
Imprime cada palabra apenas encuentra un espacio (sin split()), y la última al terminar.
"""
frase = input("Ingrese una frase:")

palabra = ""
for c in frase:
    if c == " ":
        print(palabra)
        palabra = ""
    else:
        palabra += c

print(palabra)