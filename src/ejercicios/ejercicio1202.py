
"""Este programa solicita el ingreso de un número entero y determina si el
valor ingresado es mayor que 10 o no es mayor a 10, informando el resultado correspondiente
al usuario."""

num = int(input("Ingrese un numero entero: "))

mensaje = ""

if num > 10:
    print("El numero es mayor que 10.")
elif num < 10:
    print("El numero es menor que 10.")
else:
    print("El numero es igual a 10.")
