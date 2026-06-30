""" en este ejercicio vamos a pedir el ingreso de una cadena de caracteres y luego un caracter a reemplaza en la cadena
luego imprimiremos la cadena con el caracter reemplazado"""
cadena = input("ingrese cadena de caracateres: ").lower()
caracter = input("ingrese caracter a reemplazar: ").lower()
cadena_final = ""
for letra in cadena:
    if letra == caracter:
        cadena_final += "*"
    else:
        cadena_final += letra
print(cadena_final)