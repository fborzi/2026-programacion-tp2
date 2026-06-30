"""Este programa solicita el ingreso de una cadena de texto e informe
la cantidad de palabras que posee la cadena y la cantidad de caracteres
que posee cada palabra"""


cadena = input("Ingrese una cadena de texto: ")

cantidad_palabras = 0
i = 0

while i < len(cadena):

    while i < len(cadena) and cadena[i] == " ":
        i += 1

    if i == len(cadena):
        break

    cantidad_palabras += 1
    palabra = ""
    letras = 0

    while i < len(cadena) and cadena[i] != " ":
        palabra += cadena[i]
        letras += 1
        i += 1

    print("La palabra", "'" + palabra + "'", "tiene", letras, "letras.")

print("La cantidad de palabras en la cadena es:", cantidad_palabras)