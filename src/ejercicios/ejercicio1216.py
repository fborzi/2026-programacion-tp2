frase = input("Ingrese una frase: ")
caracter = input("Ingrese el caracter a reemplazar: ")
while len(caracter) != 1:
    print("Debe ingresar un solo caracter.")
    caracter = input("Ingrese el caracter a reemplazar: ")
nueva_frase = ""
for c in frase:
    if c == caracter:
        nueva_frase += "*"
    else:
        nueva_frase += c
print("Frase resultante:", nueva_frase)
