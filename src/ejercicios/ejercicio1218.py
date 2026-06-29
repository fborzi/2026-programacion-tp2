"""Solicito al usuario ingresar el titulo de su libro favorito y lo convierto a minusculas con .lower().
Creo nueva_frase combinando dos partes:
- titulo_libro[0].upper() accede a la primera letra con indexing y la convierte a mayuscula
- titulo_libro[1:] accede al resto del string desde el segundo caracter en adelante con slicing
Al unirlas formo el titulo con el formato correcto y lo imprimo."""

titulo_libro = input("Ingrese el titulo de su libro favorito: ").lower()
nueva_frase = titulo_libro[0].upper() + titulo_libro[1:]
print(f"Tu libro preferido es: {nueva_frase} ")
