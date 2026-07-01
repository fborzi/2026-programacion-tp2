""" en este ejercicio pediremos el ingreso de una cadena de caracteres, buscaremos y mostraremos las
vocales utilizadas"""
vocales_cadena = ""
cadena = input("ingrese cadena de caracteres: ").lower()
if cadena.count("a") > 0:
    vocales_cadena += "a "
if cadena.count("e") > 0:
    vocales_cadena += "e "
if cadena.count("i") > 0:
    vocales_cadena += "i "
if cadena.count("o") > 0:
    vocales_cadena += "o "
if cadena.count("u") > 0:
    vocales_cadena += "u "
print("las vocales utilizadas en la cadena son:", vocales_cadena)
