"escribi un programa que pide al usuario el título de su libro preferido y lo muestre con la primera letra en mayúscula y el resto en minúscula."

titulo = input("")

titulo = titulo.strip().lower()

resultado = titulo[0].upper() + titulo[1:]

print("Tu libro preferido es " + resultado)
