"""En este ejercicio pediremos el ingreso de una cadena de caracteres en el cual contaremos cantidad de 
palabras de la cadeba de caracteres y la cantidad de letras de cada palabra"""
cadena = input("ingrese cadena de caracteres: ")
cantidad_palabras = 0
letras = 0
palabra = ""
for caracter in cadena:
    if caracter != " ":
        palabra = palabra + caracter
        letras = letras + 1
    elif letras > 0:
            cantidad_palabras = cantidad_palabras + 1
            print("La palabra", '"' + palabra + '"', "tiene", letras, "letras.")
            palabra = ""
            letras = 0
if letras > 0:
    cantidad_palabras = cantidad_palabras + 1
    print("La palabra", '"' + palabra + '"', "tiene", letras, "letras.")
print("La cantidad de palabras en la cadena es:", cantidad_palabras)