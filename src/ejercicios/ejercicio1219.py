frase = input("Ingrese una frase: ")

palabra = ""

for letra in frase:
    if letra != " ":
        palabra += letra
    else:
        print(palabra)
        palabra = ""

print(palabra)
