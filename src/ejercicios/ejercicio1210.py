total = 0

while True:
    monto = float(input())

    if monto == 0:
        break

    if monto < 0:
        print("El monto ingresado es negativo.")
    else:
        total = total + monto

print("La suma total de las ventas es:", total)