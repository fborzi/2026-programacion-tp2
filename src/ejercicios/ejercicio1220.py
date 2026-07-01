abcdario = "abcdefghijklmnñopqrstuvwxyz"
corrimiento = 2
fraseEncriptada=""
cadena= input("Ingresa una frase:").lower()

for letra in cadena :
    if letra in abcdario :
        indice_actual = abcdario.index(letra)
        nuevoIndice = (indice_actual + corrimiento) % 27
        fraseEncriptada = fraseEncriptada + abcdario[nuevoIndice] 
    else :
        fraseEncriptada = fraseEncriptada + letra
print(fraseEncriptada)