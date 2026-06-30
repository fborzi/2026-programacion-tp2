cadena = input("Ingrese una palabra: ")
a=False
e=False
i=False
o=False
u=False

for letra in cadena:
    letra=letra.lower()
    
    if letra == "a":
        a=True
    
    elif letra=="e":
        e=True

    elif letra=="i":
        i=True
    elif letra=="o":
        o=True
    elif letra=="u":
        u=True
    
print("las vocales que aparecen son:")
if a:
    print("a")

if e:
    print("e")

if i:
    print("i")

if o:
    print("o")

if u:
    print("u")