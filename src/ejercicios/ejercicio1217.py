"""
En el ejercicio 1217 el usuario ingresa caracteres de a uno, el sistema ls va concatenando hasta que el usuario ingresa un string de longitud distinto de 1 o el caracter 0
se muestra la palabra formada.
"""

palabra = ""

caracter = input("Ingrese un caracter: ")

while len(caracter) == 1 and caracter != "0":
    palabra += caracter
    caracter = input("Ingrese un caracter: ")

print(palabra)
