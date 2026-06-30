
venta=int(input("ingrese la venta realizada:"))
monto=0
while venta!=0:
        if venta>0:
            monto+=venta
            venta=int(input("ingrese la venta realizada:"))
        else:
              print("el monto ingresado es negativo")
              venta=int(input("ingrese la venta realizada:"))

print("el monto total de ventas es:", monto)
 
 
