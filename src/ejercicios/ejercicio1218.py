titulo = input("Ingrese el titulo del libro: ").strip()

resultado = ""

for i, letra in enumerate(titulo):
    if i == 0:
        resultado += letra.upper()
    else:
        resultado += letra.lower()

print(resultado)
