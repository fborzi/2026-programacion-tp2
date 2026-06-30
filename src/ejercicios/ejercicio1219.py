frase = input("Ingrese una frase: ")


palabra = ""


frase = frase + " "

for letra in frase:
    if letra != " ":
        palabra += letra
    else:
        print(palabra)
        palabra = ""