"escribi un programa que permita ingresar el monto de las ventas de un comercio, el programa debe ir sumando las ventas ingresadas y al finalizar debe mostrar la suma total de las ventas. El programa finaliza cuando se ingresa un 0. Si se ingresa un monto negativo, el programa debe mostrar un mensaje indicando que el monto ingresado es incorrecto y no debe sumarlo a la suma total de las ventas."
ventas = float(input("Ingrese el monto de la venta o ingrese 0 para finalizar: "))
contador = 0

while ventas != 0:
    if ventas > 0:
        contador = contador + ventas
    elif ventas < 0:
        print("El monto ingresado es negativo")
    ventas = float(input("Ingrese el monto de la venta o ingrese 0 para finalizar: "))

print("La suma total de las ventas es: ", contador)
