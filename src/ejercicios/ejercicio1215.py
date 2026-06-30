""" en este ejercicio pediremos el ingreso de una cadena de caracteres, buscaremos y mostraremos las vocales utilizadas"""

Vocales = ""
cadena = input("ingrese cadena de caracteres: ").lower()
if cadena.count("a") > 0:
    Vocales += "a "
if cadena.count("e") > 0:
    Vocales += "e "
if cadena.count("i") > 0:
    Vocales += "i "
if cadena.count("o") > 0:
    Vocales += "o "
if cadena.count("u") > 0:
    Vocales += "u "
print("las vocales utilizadas en la cadena son:",Vocales)