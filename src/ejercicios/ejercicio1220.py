abecedario = "abcdefghijklmnñopqrstuvwxyz"

texto = input()
corrimiento = int(input())

resultado = ""

for letra in texto:
    if letra in abecedario:
        posicion = abecedario.index(letra)
        nueva_posicion = (posicion + corrimiento) % 27
        nueva_letra = abecedario[nueva_posicion]
        resultado = resultado + nueva_letra
    else:
        resultado = resultado + letra

print(resultado)