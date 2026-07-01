"""
El ejercicio 1204 lo que pide es que el usuario ingrese un numero y compruebe si el numero es par o impar, utilice una estructura condicional 
para indicar si el numero es par o  no, y en cualquiera de los dos casos agregue un mensaje que le indica al usuario el resultado de la comparacion. 

"""

nro1 = int(input("Ingrese un numero:"))
if nro1 % 2 == 0:
    print("El numero",nro1,"es PAR")
else:
    print("El numero",nro1,"es IMPAR")
