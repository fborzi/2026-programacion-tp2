
alfabeto = "abcdefghijklmnñopqrstuvwxyz"

texto = input("Ingrese un texto: ")
corrimiento = int(input("Ingrese la cantidad de lugares a correr: "))

texto_encriptado = ""


for letra in texto:

   
    letra_minuscula = letra.lower()

    if letra_minuscula in alfabeto:

    
        indice = alfabeto.index(letra_minuscula)

        nuevo_indice = (indice + corrimiento) % 27


        nueva_letra = alfabeto[nuevo_indice]

        if letra.isupper():
            nueva_letra = nueva_letra.upper()

        texto_encriptado += nueva_letra

    else:
        # Si no es una letra, se deja igual
        texto_encriptado += letra

