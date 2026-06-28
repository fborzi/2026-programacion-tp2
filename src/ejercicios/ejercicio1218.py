"""
En el ejercicio 1218 se pide que se ingrese el nombre de
un libro, el cual no importa si esta en mayuscula o miniscula,
la salida en pantalla va a contener la primer letra del titulo
en mayuscula y luego todo minuscula.
"""
titulo = input("Ingrese el título del libro: ")

resultado = ""

for i in range(len(titulo)):
    letra = titulo[i]

    if i == 0:
        resultado += letra.upper()
    else:
        resultado += letra.lower()

print(resultado)
