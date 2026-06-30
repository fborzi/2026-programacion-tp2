texto = input().strip()

palabra = ""
contador = 0

for c in texto:
    if c != " ":
        palabra += c
    else:
        print(palabra, len(palabra))
        contador += 1
        palabra = ""

print(palabra, len(palabra))
contador += 1

print("La cantidad de palabras en la cadena es:", contador)
