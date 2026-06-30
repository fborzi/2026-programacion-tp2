"""Este programa solicita el ingreso de los montos correspondientes a las
ventas realizadas durante una semana, finalizando la carga cuando se
ingresa un valor igual a cero. Los montos negativos se informan como
inválidos y no se consideran en el cálculo, mientras que los valores
positivos se acumulan para obtener el monto total de las ventas."""

suma_ventas = 0.0

monto = int(input("Ingrese el monto de cada venta realizada: "))

while monto != 0:

    if monto < 0:
        monto = int(input())
        continue

    suma_ventas += monto
    monto = int(input())
        
print("El monto ingresado es negativo.")
print("La suma total de las ventas es: ", suma_ventas)

