# escribi un programa que recibe un texto, un entero y aplica un cifrado de sustitución simple al texto.
# Se desplaza cada letra por el número de posiciones indicado por el entero,
# manteniendo el caso de las letras y dejando los caracteres no alfabéticos sin cambios.

ALFABETO = "abcdefghijklmnñopqrstuvwxyz"

texto = input("")
dezp = int(input(""))

resultado = ""

for char in texto:
    if char.lower() in ALFABETO:
        indice = ALFABETO.index(char.lower())
        nuevo_indice = (indice + dezp) % 27
        letra = ALFABETO[nuevo_indice]
        if char.isupper():
            letra = letra.upper()
        resultado += letra
    else:
        resultado += char

print(resultado)
