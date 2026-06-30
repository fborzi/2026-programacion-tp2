frase = input("Ingrese una frase: ")

caracter = input("Ingrese un carácter: ")

nueva_frase = ""

for letra in frase:
    if letra == caracter:
        nueva_frase += "*"
    else:
        nueva_frase += letra
