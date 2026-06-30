"""en este ejercicio pediremos una cadena de caracteres en la cual identificaremos las palabras
e imprimiremos de forma individual"""
cadena = input("ingrese cadena de caracteres: ")
palabra = ""
for caracter in cadena:
    if caracter != " ":
        palabra += caracter
    else:
        print(palabra)
        palabra = ""
print(palabra)
