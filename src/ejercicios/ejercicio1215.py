"""
En este ejercicio se pide que se ingrese una cadena de texto.
Luego vamos a buscar cuantas vocales tiene tanto en mayucula
o en minuscula, y en pantalla se va a imprimir que vocales hay.
"""
cadena = input("Ingrese una cadena: ")
cadena = cadena.lower()

a = False
e = False
i = False
o = False
u = False

for letra in cadena:
    if letra == "a":
        a = True
    elif letra == "e":
        e = True
    elif letra == "i":
        i = True
    elif letra == "o":
        o = True
    elif letra == "u":
        u = True

print("Las vocales que aparecen en la cadena son:", end=" ")

if a:
    print("a", end=" ")
if e:
    print("e", end=" ")
if i:
    print("i", end=" ")
if o:
    print("o", end=" ")
if u:
    print("u", end=" ")
