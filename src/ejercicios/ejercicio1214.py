"""en este ejercicio se pide ingresar una cadena de texto por teclado y que informe la cantidad de palbras
que posee la cadena y la cantidad de caracteres que posee cada palabra"""
cadena = input("Ingrese una cadena: ")
palabras = 0
letras = 0
palabra = ""
for caracter in cadena:
    if caracter != " ":
        palabra = palabra + caracter
        letras = letras + 1
    else:
        if palabra != "":
            palabras = palabras + 1
            print("La palabra", palabra, "tiene", letras, "letras.")
            palabra = ""
            letras = 0
if palabra != "":
    palabras = palabras + 1
    print("La palabra", palabra, "tiene", letras, "letras.")
print("La cantidad de palabras es:", palabras)
