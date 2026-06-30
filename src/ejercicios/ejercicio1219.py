frase = input()

palabra = ""
i = 0

while i < len(frase):
    if frase[i] != " ":
        palabra += frase[i]
    else:
        print(palabra)
        palabra = ""
    i += 1

print(palabra)
