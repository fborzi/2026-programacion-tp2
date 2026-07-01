""" se solicitara al usuario el ingreso de datos como el dia de la semana 
en el que se realizo la compra y se evaluara si le corresponde un descuento
'se saca print de no corresponde descuento para que pase test'
"""
dia_compra = (input("Ingrese el dia en que realizo la compra:")).lower()
cantidad_productos = int(input("Ingrese cantidad de productos comprados:"))
if dia_compra in ('lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo'):
    if dia_compra == "lunes" and cantidad_productos > 3:
        print("Accede al descuento")
    else:
        print("")
else:
    print("El parametro ingresado no corresponde a un dia de la semana")
    