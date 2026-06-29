"""en este ejercicio se pide ingresar una frase y liego un caracter de longuitud 1, mostrar la frase
ingresada pero cambiando el caracter por * """
frase = input("Ingrese una frase: ")
caracter = input("Ingrese un carácter: ")
frase_new = ""
for letra in frase:

    if letra == caracter:
        frase_new = frase_new + "*"
    else:
        frase_new  = frase_new + letra
print(frase_new)
