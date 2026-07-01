"""
Ejercicio 1210 - Ventas de la semana
Autor: Valentin Saldias
"""

cantidad = int(input("Ingrese la cantidad de ventas: "))

suma = 0

for i in range(cantidad):
    venta = float(input(f"Ingrese el monto de la venta {i + 1}: "))

    if venta < 0:
        print("El monto ingresado es negativo.")
    else:
        suma += venta

print("La suma total de las ventas es:", suma)