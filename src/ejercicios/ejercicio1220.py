""" en este ejercicio se pide encriptar un texto usando la cifra de cesar, mover cada letra del texto
una determinada  cantidad de posiciones hacia adelante en el alfabeto.
Esa cantidad de posiciones la ingresa el usuario. """
ALFABETO = "abcdefghijklmnñopqrstuvwxyz"
texto = input("Ingrese un texto: ").lower()
mover_letra = int(input("Ingrese el corrimiento: "))
resultado = ""
for letra in texto:
    if letra in ALFABETO:
        posicion = ALFABETO.index(letra)
        nueva_posicion = (posicion + mover_letra) % 27
        resultado += ALFABETO[nueva_posicion]
    else:
        resultado += letra
print(resultado)
