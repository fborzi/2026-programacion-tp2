"""Escribi un programa que solicite el ingreso del monto de cada venta realizada en una tienda
durante la ultima semana. Luego, se debera mostrar el monto total de las ventas. Si se lee un
monto negativo, se debe informar el problema sin interrumpir el ingreso de los datos. La
lectura de la informacion finaliza al leer un monto igual a cero."""

montode_venta = 1
monto_total = 0

while montode_venta != 0 :
    montode_venta = float(input("ingrese el monto de la venta"))
    if montode_venta < 0 :
        print("El monto ingresado es negativo.")
    else :
        monto_total = monto_total + montode_venta

print(f"La suma total de las ventas es: {monto_total}")
