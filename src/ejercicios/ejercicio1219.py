"""Este programa permite ingresar una frase, imprima una por una las palabras que la contienen, 
por cada palabra exista un espacio entre ellas y que no exista espacio al final ni al comienzo, no
es posible usar split()"""

frase = input("Ingrese una frase: ")
palabra = ""
for caracter in frase:
    if caracter != " ":
        palabra += caracter
    else:
        if palabra:
            print(palabra)
            palabra = ""