texto = input("ingrese el texto a encriptar: ").lower()
corrimiento = int(input("ingrese la cantidad de lugares: "))

abecedario = "acbdefghijklmnñopqrstuvwxyz"
texto_encriptado = ""

for letra in texto:
    
    if letra not in abecedario:
        texto_encriptado = texto_encriptado
    else:
        indice = abecedario.find(letra)
        nuevo_indice = (indice + corrimiento) % 27
        letra_nueva = abecedario[nuevo_indice]
        texto_encriptado = texto_encriptado +letra_nueva
        
print(texto_encriptado)