"""
En este ejercicio se pide que se ingrese una frase cualquiera,
lueggo un caracter que puede ser una vocal. Luego en pantalla
va a resaltar la frase, pero por cada letra que se eligio para
el caracter será reemplaza por un asterisco.
"""
frase = input("Ingrese una frase: ")
caracter = input("Ingrese un carácter: ")

resultado = ""

for letra in frase:
    if letra == caracter:
        resultado += "*"
    else:
        resultado += letra

print(resultado)
