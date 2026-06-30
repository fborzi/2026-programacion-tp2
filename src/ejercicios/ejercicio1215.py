"""en este ejercicio pide ingresar una cadena e informar las vocales sin repetir"""
cadena = input("Ingrese una cadena: ")
cadena = cadena.lower()
a = False
e = False
i = False
o = False
u = False
for letra in cadena:
    if letra == "a" and not a:
        print("a")
        a = True
    elif letra == "e" and not e:
        print("e")
        e = True
    elif letra == "i" and not i:
        print("i")
        i = True
    elif letra == "o" and not o:
        print("o")
        o = True
    elif letra == "u" and not u:
        print("u")
        u = True
