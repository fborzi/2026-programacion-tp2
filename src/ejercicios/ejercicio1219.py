frase = input("ingrese una frase: ")

palabra_actual = ""

for letra in frase:
    if letra !=" ":
        palabra_actual = palabra_actual + letra
    else:
        print(palabra_actual)
        palabra_actual = ""
        
print(palabra_actual)