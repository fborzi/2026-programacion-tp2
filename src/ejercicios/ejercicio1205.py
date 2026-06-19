"Escribi un programa que solicite al usuario un día de la semana y la cantidad de productos que desea comprar. Si el día es lunes y la cantidad de productos es mayor a 3, el programa debe mostrar un mensaje indicando que el usuario accede a un descuento."
dia = str.lower(input("Ingrese un día de la semana: ").lower())
productos = int(input("Ingrese el producto que desea comprar: "))

if dia == "lunes" and productos > 3:
    print("accede al descuento")