total_ventas = 0
contador_ventas = 1
while True:
    monto = float(input(f"ingresa el monto de la venta{contador_ventas}. 0 para terminar: "))
    if monto == 0:
        break # 0 corta la carga 
    if monto < 0:
        print("error: no se puede ingresar un monto negativo. se ignora ")
        continue # se ignora y pide el siguiente 
    total_ventas += monto # solo suma si es positivo
    contador_ventas += 1
    print("/n---Cierre de Semana ---")
    print(f"Monto total de las ventas : $ {total_ventas:.2f}")
    