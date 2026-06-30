texto = input()

texto = texto.strip()  # elimina espacios al inicio y final

palabras = 0
en_palabra = False
longitud = 0
resultado = []

i = 0
while i < len(texto):
    if texto[i] != " ":
        if not en_palabra:
            en_palabra = True
            palabras += 1
            longitud = 1
        else:
            longitud += 1
    else:
        if en_palabra:
            resultado.append(longitud)
            en_palabra = False
        longitud = 0
    i += 1

# agregar última palabra si termina en letra
if en_palabra:
    resultado.append(longitud)

print("La cantidad de palabras en la cadena es:", palabras)

# reconstruir palabras para mostrar (sin split)
texto += " "
palabra = ""
indice = 0

for c in texto:
    if c != " ":
        palabra += c
    else:
        if palabra != "":
            print("la palabra '" + palabra.capitalize() + "' tiene", resultado[indice], "letras")
            indice += 1
            palabra = ""
