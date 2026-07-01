"""
Ejercicio 1205 - Descuento en tienda
Autor: Valentin Saldias
"""

dia = input("Ingrese el día de la semana: ")
cantidad = int(input("Ingrese la cantidad de artículos comprados: "))

if dia.lower() == "lunes" and cantidad > 3:
    print("Accede al descuento.")