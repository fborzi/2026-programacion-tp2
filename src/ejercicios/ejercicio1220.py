frase = input("Ingrese una frase: ")
corrimiento = int(input("Ingrese el corrimiento: "))

abecedario = "abcdefghijklmnopqrstuvwxyz"
resultado = ""

for letra in frase:
    if letra in abecedario:
        posicion = abecedario.index(letra)
        nueva_posicion = (posicion + corrimiento) % 26
        resultado += abecedario[nueva_posicion]
    else:
        resultado += letra

print(resultado)