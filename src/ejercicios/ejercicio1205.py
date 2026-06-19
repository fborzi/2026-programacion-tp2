"""
En este ejercicio se pide que se ingrese un dia y la cantidad de articulos
que se compra, si el dia es lunes y la cantidad de articulos es mayor que 3
accede al descuento.
"""
dia = input("Ingrese el día de la semana: ")
articulos = int(input("Ingrese la cantidad de artículos: "))

if dia.lower() == "lunes" and articulos > 3:
    print("Accede al descuento.")
    