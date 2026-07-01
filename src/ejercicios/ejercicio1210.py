"""En este ejercicio pediremos el ingreso de valor de las ventas semanales y calcularemos el monto total
de las mismas, como tambien informaremos si el dato ingresado no corresponde a lo esperado, si es negativo"""
venta_semanal = 0
venta = float(input("ingrese monto de la venta: "))
while venta != 0:
    if venta > 0:
        venta_semanal = venta_semanal + venta
    else:
        print("el monto ingresado es negativo")
    venta = float(input("ingrese monto de la venta: "))
print("la suma del total de las ventas es: ", venta_semanal)
