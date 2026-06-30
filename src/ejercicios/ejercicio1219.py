frase = input("Ingresá una frase: ")

palabra = ""

for letra in frase:
    if letra == " ":
        print(palabra)
        palabra = ""
    else:
        palabra += letra

print(palabra)