"""en este ejercicio se pide ingresar por teclado el monto de cada venta en una tienda en una semana,
mostrar el monto total y si hay un monto negativo se debe informar sin interrumpir el programa,
finaliza cuando se ingrese un monto igual a 0"""
suma = 0 
monto = float(input("Ingrese el monto de la venta: "))
while monto != 0 :
    if monto < 0:
        print("El monto ingresado es negativo.")
    else:
        suma = suma + monto
        monto = float(input("Ingrese el monto de la venta: "))
print ("La suma total de las ventas es:", suma)
