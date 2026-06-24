titulo = input("Ingrese el titulo del libro: ").strip()

resultado = ""

for i in range(len(titulo)):
    if i == 0:
        resultado += titulo[i].upper()
    else:
        resultado += titulo[i].lower()

print(resultado)