"""
En el siguiente codigo, se pide al usuario que ingrese el monto de las ventas,
asi poder sumar el total. En el caso que se una venta negativa no se resta, solo
suma el resultado de lo vendido.
"""
total_ventas = 0.0

while True:
    monto = float(input("Ingrese el monto de la venta: "))

    if monto == 0:
        break

    if monto < 0:
        print("El monto ingresado es negativo.")
    else:
        total_ventas += monto

print("La suma total de las ventas es:", total_ventas)
