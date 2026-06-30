"""Identifica las vocales presentes en un texto"""
cadena = input("Ingrese una cadena: ").lower()

vocales = ""

if "a" in cadena:
    vocales += "a"
if "e" in cadena:
    vocales += "e"
if "i" in cadena:
    vocales += "i"
if "o" in cadena:
    vocales += "o"
if "u" in cadena:
    vocales += "u"

print("Las vocales que aparecen en la cadena son:", vocales)
