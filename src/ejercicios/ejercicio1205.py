""" se solicitara al usuario el ingreso de datos como el dia de la semana 
en el que se realizo la compra y se evaluara si le corresponde un descuento
"""
diaCompra = (input("Ingrese el dia en que realizo la compra:")).lower()
CantidaProductos = int(input("Ingrese cantidad de productos comprados:"))

if diaCompra == "lunes" or diaCompra == "martes" or diaCompra == "miercoles" or diaCompra == "jueves" or diaCompra == "viernes" or diaCompra == "sabado" or diaCompra == "domingo":
    if diaCompra == "lunes" and CantidaProductos > 3:
        print("Accede al descuento")
    else:
        print("No le corresponde un descuento")
else:
    print("El dia ingresado no es valido")