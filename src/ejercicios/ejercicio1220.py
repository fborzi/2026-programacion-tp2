frase = input("Ingrese una frase: ")
corrimiento = int(input("Ingrese el corrimiento: "))

ABECEDARIO = "abcdefghijklmnopqrstuvwxyz"
resultado = ""

for letra in frase:
    if letra in ABECEDARIO:
        posicion = ABECEDARIO.index(letra)
        nueva_posicion = (posicion + corrimiento) % 26
        resultado += ABECEDARIO[nueva_posicion]
    else:
        resultado += letra

print(resultado)
