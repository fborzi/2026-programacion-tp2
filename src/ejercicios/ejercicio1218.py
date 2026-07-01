"""Ejercicio 1218 - Formar título de libro"""

libro_ingresado = input("Ingresá el título de tu libro preferido: ")

resultado = ""
indice = 0

for caracter in libro_ingresado:
    if indice == 0:
        resultado += caracter.upper()
    else:
        resultado += caracter.lower()
    
    indice += 1

print(f"Tu libro preferido es: {resultado}")