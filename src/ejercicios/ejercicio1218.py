"""Este programa formatea un título con la primera letra en mayúscula y el resto en minúscula."""
titulo = input("ingrese el titulo de su libro preferido: ")

titulo_miniscula = titulo.lower()

primera_letra = titulo_miniscula[0].upper()

resto = titulo_miniscula[1:]

titulo_formateado = primera_letra + resto

print(titulo_formateado)