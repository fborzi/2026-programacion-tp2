cadena = input("Ingrese una cadena: ")

cadena = cadena.lower()

a = False
e = False
i = False
o = False
u = False

print("Las vocales que aparecen en la cadena son:", end=" ")

for letra in cadena:

    if letra == "a" and not a:
        print("a", end=" ")
        a = True

    elif letra == "e" and not e:
        print("e", end=" ")
        e = True

    elif letra == "i" and not i:
        print("i", end=" ")
        i = True

    elif letra == "o" and not o:
        print("o", end=" ")
        o = True

    elif letra == "u" and not u:
        print("u", end=" ")
        u = True