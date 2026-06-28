"""
En este ejercicio lo que se hace es definir es una variable todo el abecedario.
luego se pide que en otra variable se guarde un texto el cual pedimos que se ingrese.
despues se pide que cantidad de letras queremos que se imprima en pantalla 
para encriptar el codigo. por ejemplo si el texto es hola y el corrimiento es 2,
se va a imprimir en pantalla jqnc.
"""
alfabeto = "abcdefghijklmnñopqrstuvwxyz"

texto = input("Ingrese un texto: ").lower()
corrimiento = int(input("Ingrese el corrimiento: "))

resultado = ""

for letra in texto:
    if letra in alfabeto:
        indice = alfabeto.index(letra)
        nuevo_indice = (indice + corrimiento) % 27
        resultado += alfabeto[nuevo_indice]
    else:
        resultado += letra

print(resultado)
