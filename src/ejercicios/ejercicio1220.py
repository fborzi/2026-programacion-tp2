"""Este programa solicita al usuario un texto y una cantidad de posiciones
de corrimiento para aplicar el cifrado César. Cada letra del texto se
desplaza la cantidad indicada dentro del alfabeto, volviendo a comenzar
desde el inicio cuando se supera la última letra. Los caracteres que no
son letras se mantienen sin modificaciones y, al finalizar, se muestra
el texto encriptado."""

ALFABETO = "abcdefghijklmnñopqrstuvwxyz"

texto = input("Ingresar texto a encriptar: ").lower()
corrimiento = int(input("Ingese la cantidad de lugares en correr cada letra: "))

resultado = ""

for letra in texto:

    if letra in ALFABETO:

        indice = ALFABETO.index(letra)
        nuevo_indice = (indice + corrimiento) % len(ALFABETO)
        resultado += ALFABETO[nuevo_indice]

    else:
        resultado += letra

print(resultado)