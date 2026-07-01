"""
Suma montos de venta hasta ingresar 0; avisa si un monto es negativo sin sumarlo.
"""
suma = 0.0

while True:
    monto = float(input("Ingrese monto: "))
    if monto == 0:
        break
    if monto < 0:
        print("El monto ingresado es negativo.")
        continue
    suma += monto

print(f"La suma total de las ventas es: {suma}")
