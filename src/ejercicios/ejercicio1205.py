"""en este ejercicio se pide ingrresar por teclado el dia de la semana y los articulos comprados
por el cliente a ver si accede o no al descuento"""
dia = input("Ingrese el dia de la semana:")
articulos = int(input("Ingrese la cantidad de articulos comprados:"))
if dia == "lunes" and articulos >= 3:
    print("Accede al descuento.")
