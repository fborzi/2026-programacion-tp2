"""en este ejercicio se pide ingresar una frase e imprimir las palabras 1 por 1, separadas por espacio
y sin espacios al principio y al final de la frase ingresada"""
frase = input("Ingrese una frase: ")
palabra = ""
for letra in frase:
    if letra != " ":
        palabra += letra
    else:
        print(palabra)
        palabra = ""
print(palabra)
