texto = input()
car = input()

resultado = ""

for c in texto:
    if c.lower() == car.lower():
        resultado += "*"
    else:
        resultado += c

print(resultado)
