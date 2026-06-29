"""
El ejercicio 1203 

"""

x = int(input("Ingrese el primer numero:"))
y = int(input("Ingrese el segundo numero:"))

if x < y:
    print(x,"es menor que",y)
else:
    if x > y:
        print(x,"es mayor que",y)

    else:
        if x == y:
            print(x,"es igual a",y)
  