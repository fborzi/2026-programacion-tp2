"""
Arma un nuevo string reemplazando manualmente coincidencias por "" (sin replace()).*
"""
frase = input("Ingrese frase:")
caracter = input("Ingrese caracter a reemplazar por *:")

resultado = ""
for c in frase:
    if c == caracter:
        resultado += "*"
    else:
        resultado += c

print(resultado)