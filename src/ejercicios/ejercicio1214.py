"""En este ejercicio pediremos el ingreso de una cadena de caracteres en el cual contaremos cantidad de
palabras de la cadeba de caracteres y la cantidad de letras de cada palabra"""
texto = input("ingrese cadena de caracteres: ")
cadena = texto.strip()
cant_pala = 0
letra = 0
palabra = ""
for caracter in cadena:
    if caracter != " ":
        letra = letra + 1
    elif letra > 0:
        cant_pala = cant_pala + 1
        letra = 0
print("La cantidad de palabras en la cadena es:", cant_pala + 1)
letra = 0
for caracter in cadena:
    if caracter != " ":
        palabra = palabra + caracter
        letra = letra + 1
    elif letra > 0:
            print("La palabra", '"' + palabra + '"', "tiene", letra, "letras.")
            palabra = ""
            letra = 0
if letra > 0:
    print("La palabra", '"' + palabra + '"', "tiene", letra, "letras.")
