"""
En este ejercicio se pide que se ingrese un caracter,
y asi hasta que decida ingresar el numero 0. Entonces
en pantalla va a aparecer una cadena completa.
"""
cadena = ""

while True:
    caracter = input("Ingrese un carácter: ")

    if len(caracter) != 1 or caracter == "0":
        break

    cadena += caracter

print(cadena)
