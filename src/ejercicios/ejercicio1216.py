"""Reemplaza un caracter especifico por asteriscos en una cadena"""
frase = input("Ingrese una frase: ")
caracter = input("Ingrese un caracter: ")

nueva_frase = " "

for letra in frase:
    if letra.lower() == caracter.lower():
        nueva_frase += "*"
    else:
        nueva_frase += letra

print(nueva_frase)
