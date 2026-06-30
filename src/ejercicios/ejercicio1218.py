"""Este programa solicita al usuario el ingreso del título de un libro preferido.
Primero convierte todo el texto a minúsculas para normalizarlo y luego separa
el título en palabras utilizando espacios como separador.
Después recorre cada palabra y la formatea colocando la primera letra en mayúscula
y el resto en minúscula, construyendo un nuevo string con el formato correcto.
Finalmente muestra el título del libro con el formato: primera letra de cada palabra
en mayúscula y las demás en minúscula, independientemente de cómo lo haya ingresado el usuario."""

titulo = input("Ingrese el título de su libro preferido: ")

titulo = titulo.lower()

palabras = titulo.split()

resultado = ""

for palabra in palabras:
    resultado += palabra[0].upper() + palabra[1:] + " "

print (resultado)
