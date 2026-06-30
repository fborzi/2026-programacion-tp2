frase = input()
car = input()

resultado = ""

for c in frase:
    if c == car:
        resultado += "*"
    else:
        resultado += c

print(resultado)
