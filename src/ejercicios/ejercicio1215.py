"""en este ejercicio pide ingresar una cadena e informar las vocales sin repetir"""
cadena = input("Ingrese una cadena: ")
cadena = cadena.lower()
a = False
e = False
i = False
o = False
u = False
print("Las vocales que aparecen en la cadena son: ")
for letra in cadena:

    if letra == "a" and a == False:
        print("a")
        a = True

    elif letra == "e" and e == False:
        print("e")
        e = True

    elif letra == "i" and i == False:
        print("i")
        i = True

    elif letra == "o" and o == False:
        print("o")
        o = True

    elif letra == "u" and u == False:
        print("u")
        u = True
