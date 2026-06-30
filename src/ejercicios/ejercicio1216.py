"""Este programa solicita al usuario que ingrese una frase y un carácter (string de longitud 1).
Luego recorre la frase letra por letra y reemplaza todas las apariciones del carácter ingresado
por el símbolo "*".
Como no se permite utilizar la función replace(), el programa construye una nueva cadena
comparando cada letra de la frase con el carácter ingresado y agregando "*" o la letra original
según corresponda.
Finalmente, muestra la frase modificada en pantalla."""

frase = input("Ingrese una frase: ")
caracter = input("Ingrese un caracter: ")

resultado = ""

for letra in frase:
    if letra == caracter:
        resultado += "*"
    else:
        resultado += letra

print(resultado)
