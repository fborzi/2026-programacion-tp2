"""
Informa descuento solo si el día es lunes y se compraron más de 3 artículos.
"""
dia = input("Ingrese qué día es (en formato lunes|martes|miercoles,etc):")
cantidad = int(input("Ingrese la cantidad de productos que compró:"))

if dia.lower() == "lunes" and cantidad > 3:
    print("Accede al descuento.")