"""en este ejercicio se pide ingresar una cadena de texto por teclado y que informe la cantidad de palbras
que posee la cadena y la cantidad de caracteres que posee cada palabra"""
cadena = input("Ingrese una cadena: ")
palabras = 0
letras = 0
palabra = ""
for caracter in cadena:
    if caracter != " ":
        if palabra == "":
            palabras += 1
        palabra += caracter
    else:
        palabra = ""
print("La cantidad de palabras es:", palabras)
palabra = ""
letras = 0
for caracter in cadena:
    if caracter != " ":
        palabra += caracter
        letras += 1
    else:
        if palabra != "":
            print("La palabra", palabra, "tiene", letras, "letras.")
            palabra = ""
            letras = 0
if palabra != "":
    print("La palabra", palabra, "tiene", letras, "letras.")
