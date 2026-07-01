"""
Pone en mayúscula solo la primera letra y el resto en minúscula, sin capitalize().
"""
titulo = input("Ingrese el titulo su libro preferido: ").strip()

resultado = ""
for i, c in enumerate(titulo):
    if i == 0:
        resultado += c.upper()
    else:
        resultado += c.lower()

print(resultado)
