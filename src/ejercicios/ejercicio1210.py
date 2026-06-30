"""inicialice montode_venta en 1 para entrar al bucle y monto_total en cero para acumular las ventas.
utilice un while para repetir el ingreso hasta que el usuario ingrese cero, si el monto es negativo
aviso al usuario sin interrumpir el ingreso, si es positivo lo sumo al total. al finalizar imprimo
el monto total de las ventas."""

montode_venta = 1
monto_total = 0

while montode_venta != 0:
    montode_venta = float(input("ingrese el monto de la venta: "))
    if montode_venta < 0:
        print("El monto ingresado es negativo.")
    else:
        monto_total = monto_total + montode_venta

print(f"La suma total de las ventas es: {monto_total}")
