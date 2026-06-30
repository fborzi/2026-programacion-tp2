
total_ventas = 0

monto = float(input("Ingrese el monto de la venta (0 para finalizar): "))

while monto != 0:
    if monto < 0:
        print("Error: se ingresó un monto negativo.")
    else:
        total_ventas += monto

    monto = float(input("Ingrese el monto de la venta (0 para finalizar): "))

print("El monto total de las ventas es:", total_ventas)