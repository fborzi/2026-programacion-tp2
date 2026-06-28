"""Este programa solicita el ingreso de un numero mayor de 1 y
informar si el numero es primo o no"""

numero = int(input("Ingrese un número mayor que 1: "))

if numero <= 1:
    print("Debe ingresar un número mayor que 1.")
else:
    es_primo = True

    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break

    if es_primo:
        print("El número",numero,"es PRIMO.")
    else:
        print("El número",numero," no es PRIMO.")