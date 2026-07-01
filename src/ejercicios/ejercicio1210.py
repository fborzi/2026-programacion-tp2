total = 0.0

monto = float(input())
while monto != 0:
    if monto < 0:
        print("el monto ingresado es negativo.")
    else:
        total = total + monto
        
    monto = float(input())
        
print(f"la suma total de las ventas es: {total}")        