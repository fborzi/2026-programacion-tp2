titulo = input("ingrese el titulo de su libro preferido: ")

titulo_miniscula = titulo.lower()

primera_letra_mayus = titulo_miniscula[0].upper()

resto_titulo = titulo_miniscula[1:]

titulo_formateado = primera_letra_mayus + resto_titulo

print("tu libro preferido es:", titulo_formateado)