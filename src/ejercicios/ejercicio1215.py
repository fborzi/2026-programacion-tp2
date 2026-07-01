"""
Ejercicio 1215, el usuario ingresa una cadena y el sistema leindica las vocales qe se encuentran en la cadena, para 
eso utilice una estructura repetitiva y dentro de ella una estructura condicional para identificar las vocales.
"""
cadena = input("Ingrese una cadena:")

vocales = ""

for letras in cadena.lower():
    if letras in "aeiou" and letras not in vocales:
        vocales += letras

print("Las vocales que aparecen en la cadena son:", vocales)