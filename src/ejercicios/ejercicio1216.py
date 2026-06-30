frase = input("Ingresá una frase: ")
caracter = input("Ingresá un carácter: ")

resultado = ""

for letra in frase:
    if letra == caracter:
        resultado += "*"
    else:
        resultado += letra

print(resultado)