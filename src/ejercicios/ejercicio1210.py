corte = int(input("Ingrese monto de la venta:"))
totalVentas = 0

while corte != 0 :
    if corte > 0 :
        totalVentas = totalVentas + corte  
    else :
        print("El numero es negativo")
    corte = int(input("Ingrese monto de la venta:"))   
print("El total de las ventas es:", totalVentas)