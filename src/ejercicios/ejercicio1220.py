abecedario = "abcdefghijklmnñopqrstuvwxyz"

texto = input() 
corrimiento = int(input())

texto_cifrado = ""

for letra in texto:
    if letra in abecedario:
        indice = abecedario.index(letra)
        nuevo_indice = (indice + corrimiento)
        texto_cifrado = texto_cifrado + abecedario[nuevo_indice]
    else:
        texto_cifrado = texto_cifrado + letra

print(texto_cifrado)