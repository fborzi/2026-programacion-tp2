"""
Corre cada letra según el alfabeto español de 27 letras (con ñ) usando (índice + corrimiento) % 27,
dejando intactos los caracteres que no son letras.
"""
frase = input("Ingrese frase:")
corrimiento = int(input("Ingrese el corrimiento:"))

alfabeto = "abcdefghijklmnopqrstuvwxyz"

resultado = ""
for c in frase:
    if c.lower() in alfabeto:
        es_mayuscula = c.isupper()
        indice = alfabeto.index(c.lower())
        nuevo_indice = (indice + corrimiento) % 27
        nueva_letra = alfabeto[nuevo_indice]
        if es_mayuscula:
            nueva_letra = nueva_letra.upper()
        resultado += nueva_letra
    else:
        resultado += c

print(resultado)