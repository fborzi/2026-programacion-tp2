titulo = input("Ingrese el título de su libro preferido: ")

titulo = titulo.lower()

if len(titulo) > 0:
    titulo = titulo[0].upper() + titulo[1:]

