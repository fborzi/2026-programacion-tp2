"""Este programa solicita el ingreso de un monto por venta realizada en una tienda durante la ultima semana
, luego se debera mostrar el monto total de las ventas, si lee un numero negativo se debera mostrar}
sin interrumpir el ingreso de datos, la lectura finaliza cuando se ingresa un monto igual a 0"""


monto = float(input("Ingrese el monto de la venta realizada: "))

total_ventas = 0.0

while monto != 0:
    if monto < 0:
        print("El monto ingresado es negativo")
    else:
        total_ventas = total_ventas + monto
    monto = float(input("Ingrese el monto de la venta realizada: "))

print("El monto total de las ventas es: ", total_ventas)