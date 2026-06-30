texto = input().lower()

a = False
e = False
i = False
o = False
u = False

for c in texto:
    if c == "a":
        a = True
    elif c == "e":
        e = True
    elif c == "i":
        i = True
    elif c == "o":
        o = True
    elif c == "u":
        u = True

print("las vocales que aparecen en la cadena son:", end="")

if o:
    print(" o", end="")
if a:
    print(" a", end="")
if e:
    print(" e", end="")
if i:
    print(" i", end="")
if u:
    print(" u", end="")
