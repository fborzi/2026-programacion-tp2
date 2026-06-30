"escribi un programa que recibe un texto y un número entero como entrada, y aplica un cifrado de sustitución simple al texto. Se desplaza cada letra del texto por el número de posiciones indicado por el entero, manteniendo el caso de las letras y dejando los caracteres no alfabéticos sin cambios."

alfabeto = "abcdefghijklmnñopqrstuvwxyz"

texto = input("")
dezp = int(input(""))

resultado = ""

for char in texto:
    if char.lower() in alfabeto:
        indice = alfabeto.index(char.lower())
        nuevo_indice = (indice + dezp) % 27
        letra = alfabeto[nuevo_indice]
        if char.isupper():
            letra = letra.upper()
        resultado += letra
    else:
        resultado += char

print("El texto cifrado es: " + resultado)
