"""
En el ejercicio 1218 el usuario ingresa el título de su libro preferido,el programa muestra el título con la primera letra en mayúscula
y el resto en minúscula, sin utilizar capitalize().
"""

titulo = input("Ingrese el titulo del libro: ")

primera_letra = titulo[0].upper()
resto = titulo[1:].lower()

titulo_formateado = primera_letra + resto

print(titulo_formateado)
