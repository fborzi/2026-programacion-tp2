"""
En el ejercicio 1216 el usuario ingresa una frase y un carácter, el sistema remplaza todas las apariciones de ese caracter po *
"""

frase = input("Ingrese una frase: ")
caracter = input("Ingrese un caracter: ")

nueva_frase = ""

for letra in frase:
    if letra == caracter:
        nueva_frase += "*"
    else:
        nueva_frase += letra

print(nueva_frase)
