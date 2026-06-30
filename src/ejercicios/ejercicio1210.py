monto = float(input("Ingrese el monto de la venta: "))

suma_ventas = 0

while monto != 0:
    if monto < 0:
        print("El monto ingresado es negativo.")
    else:
        suma_ventas += monto
    monto = float(input("Ingrese el monto de la venta: "))
print("La suma total de las ventas es:", suma_ventas)
