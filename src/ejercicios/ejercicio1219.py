"escribi un programa que recibe una frase y la imprime palabra por palabra, cada una en una línea diferente."

frase = input("")

palabra_actual = ""

for char in frase:
    if char != " ":
        palabra_actual += char
    else:
        if palabra_actual != "":
            print(palabra_actual)
            palabra_actual = ""

# Imprimir la última palabra
if palabra_actual != "":
    print(palabra_actual)
