"""Corre cada letra segun el alfabeto espanol de 27 letras (con ene), dejando intactos los demas caracteres."""
frase = input("Ingrese frase:")
corrimiento = int(input("Ingrese el corrimiento:"))

ALFABETO = "abcdefghijklmn\u00f1opqrstuvwxyz"

resultado = ""
for c in frase:
    if c.lower() in ALFABETO:
        es_mayuscula = c.isupper()
        indice = ALFABETO.index(c.lower())
        nuevo_indice = (indice + corrimiento) % 27
        nueva_letra = ALFABETO[nuevo_indice]
        if es_mayuscula:
            nueva_letra = nueva_letra.upper()
        resultado += nueva_letra
    else:
        resultado += c

print(resultado)