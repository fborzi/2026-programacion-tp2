""" en este ejercicio pediremos el ingreso de una cadena de caracteres, buscaremos y mostraremos las
vocales utilizadas"""

Vocal_Snake = ""
cadena = input("ingrese cadena de caracteres: ").lower()
if cadena.count("a") > 0:
    Vocal_Snake += "a "
if cadena.count("e") > 0:
    Vocal_Snake += "e "
if cadena.count("i") > 0:
    Vocal_Snake += "i "
if cadena.count("o") > 0:
    Vocal_Snake += "o "
if cadena.count("u") > 0:
    Vocal_Snake += "u "
print("las vocales utilizadas en la cadena son:",Vocal_Snake)
