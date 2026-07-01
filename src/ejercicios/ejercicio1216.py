"""Este programa solicita el al usuario ingresar una frase y luego un caracter(strign de longitud 1)
y luego muestre la frase ingresada,per con todas las ocurrencias de caracter indicado por el usuario
reemplazadas por '*' sin usar replace[]"""

frase = input("Ingrese una frase: ")
caracter = input("Ingrese un caracter (string de longitud 1): ")

frase_modificada = ""
for c in frase:
    if c == caracter:
        frase_modificada += "*"
    else:
        frase_modificada += c

print("Frase modificada:", frase_modificada)