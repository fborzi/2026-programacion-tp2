frase = input()
corrimiento = int(input())

alfabeto = "abcdefghijklmnñopqrstuvwxyz"

resultado = ""

for c in frase:
    if c.lower() in alfabeto:
        pos = alfabeto.index(c.lower())
        nueva_pos = (pos + corrimiento) % 27
        nueva_letra = alfabeto[nueva_pos]

        # mantener mayúscula si corresponde
        if c.isupper():
            resultado += nueva_letra.upper()
        else:
            resultado += nueva_letra
    else:
        resultado += c

print(resultado)
