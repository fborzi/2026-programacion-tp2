frase = input("ingrese una frase: ")
caracter = input("ingrese un caracter de longitud 1: ")

frase_nueva = ""

for letra in frase:
    
    if letra.lower() == caracter.lower():
        frase_nueva = frase_nueva + "*"
    else:
        frase_nueva = frase_nueva + letra
        
print(frase_nueva)