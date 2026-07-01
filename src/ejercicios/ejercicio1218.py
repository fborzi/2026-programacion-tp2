titulo = input("Ingrese el titulo de su libro preferido: ")
titulo = titulo.lower()
if len(titulo) > 0:
    titulo_formateado = titulo[0].upper() + titulo[1:]
else:
    titulo_formateado = ""
print("Tu libro preferido es:", titulo_formateado)
