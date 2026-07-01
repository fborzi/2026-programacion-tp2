"""
En el ejercicio 1210 se ingresan los montos de las ventas de una semana,si el monto es negativo, se informa el error pero el programa continúa
la carga finaliza al ingresar 0 y se muestra la suma total de las ventas.

"""

suma_ventas = 0

monto = float(input("Ingrese el monto de la venta: "))

while monto != 0:

    if monto < 0:
        print("El monto ingresado es negativo.")
    else:
        suma_ventas += monto

    monto = float(input("Ingrese el monto de la venta: "))

print("La suma total de las ventas es:", suma_ventas)
