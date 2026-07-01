total = 0.0  
while True:
    monto = float(input("Ingrese el monto de la venta (0 para terminar): "))
    
    if monto == 0:
        break  
    
    if monto < 0:
        print("El monto ingresado es negativo.")
        continue  
    
    total += monto  
print("La suma total de las ventas es:", total)