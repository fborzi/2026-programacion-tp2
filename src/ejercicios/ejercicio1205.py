"""Verifica si se cumplen las condiciones para
obtener un descuento"""
dia = input("Ingrese el dia de la semana: ")
articulo = int(input("Ingrese la cantidad de articulos: "))

if dia == "lunes" and articulo > 3:
    print("Accede al descuento.")
