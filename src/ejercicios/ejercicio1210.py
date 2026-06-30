suma = 0

monto = float(input())

while monto != 0:
    if monto < 0:
        print("el monto ingresado es negativo")
    else:
        suma += monto

    monto = float(input())

print("la suma total de las ventas es:", suma)
