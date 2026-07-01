"""En este ejercicio pediremos el ingreso de una cadena de caracteres en el cual contaremos cantidad de 
palabras de la cadeba de caracteres y la cantidad de letras de cada palabra"""
texto = input("ingrese cadena de caracteres: ")
cadena = texto.strip()
cant_palabras = 0
letra_palabr = 0
palab_caden = ""
for caracter in cadena:
    if caracter != " ":
        letra_palabr = letra_palabr + 1
    elif letra_palabr > 0:
            cant_palabras = cant_palabras + 1
            letra_palabr = 0
print("La cantidad de palabras en la cadena es:", cant_palabras + 1)
letra_palabr = 0
for caracter in cadena:
    if caracter != " ":
        palab_caden = palab_caden + caracter
        letra_palabr = letra_palabr + 1
    elif letra_palabr > 0:
            print("La palabra", '"' + palab_caden + '"', "tiene", letra_palabr, "letras.")
            palab_caden = ""
            letra_palabr = 0
if letra_palabr > 0:
    print("La palabra", '"' + palab_caden + '"', "tiene", letra_palabr, "letras.")
