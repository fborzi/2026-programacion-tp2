"""Forma un texto a partir de caracteres ingresados
hasta un caracter de fin"""
texto = ""

caracter = input("Ingrese un caracter:")

while len(caracter) == 1 and caracter != "0":
    texto += caracter
    caracter = input("Ingrese un caracter:")

print(texto)
