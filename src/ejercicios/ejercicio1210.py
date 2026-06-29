total = 0

cant = int(input("cuantas veces vas a cargar: "))

for i in range(cant):
    monto = float(input("monto de la venta: "))
    
    if monto < 0:
        print("el monto ingresado es negativo.")
    else:
        total = total + monto
        
print("la suma total de las ventas es:",total)            