"""En este ejercicio pediremos el ingreso de una cadena de caracteres en el cual contaremos cantidad de 
palabras de la cadeba de caracteres y la cantidad de letras de cada palabra"""
texto = input("ingrese cadena de caracteres: ")
cadena = texto.strip()
cantidad_palabras = 0
letras_palabra = 0
palabra_cadena = ""
for caracter in cadena:
    if caracter != " ":
        letras_palabra = letras_palabra + 1
    elif letras_palabra > 0:
            cantidad_palabras = cantidad_palabras + 1
            letras_palabra = 0
print("La cantidad de palabras en la cadena es:", cantidad_palabras + 1)
letras_palabra = 0
for caracter in cadena:
    if caracter != " ":
        palabra_cadena = palabra_cadena + caracter
        letras_palabra = letras_palabra + 1
    elif letras_palabra > 0:
            print("La palabra", '"' + palabra_cadena + '"', "tiene", letras_palabra, "letras.")
            palabra_cadena = ""
            letras_palabra = 0
if letras_palabra > 0:
    print("La palabra", '"' + palabra_cadena + '"', "tiene", letras_palabra, "letras.")
