"""
El ejercicio 1203 solicita que el usuario ingrese dos numeros y verifique si el primeros es mayor que el segundo, para eso use una
estructura condicional para indicar si es mayor, menor o igual y en todos los casos agregue un mensaje que le indica al usuario el resultado.

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
  