"""
Arma un nuevo string reemplazando manualmente coincidencias por "" (sin replace()).*
"""
frase = input("Ingrese frase:").lower()
caracter = input("Ingrese caracter a reemplazar por *:").lower()

resultado = ""
for c in frase:
    if c == caracter:
        resultado += "*"
    else:
        resultado += c

print(resultado)