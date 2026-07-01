"""en este ejercicio pediremos el ingreso de una cadena de caracteres y luego la imprimiremos con la primer letra en
mayuscula y el s¿resto en minuscula"""
titulo = input("Ingrese el titulo de su libro favorito: ").strip().lower()
cadena_caracteres = titulo[0].upper() + titulo[1:]
print(cadena_caracteres)
