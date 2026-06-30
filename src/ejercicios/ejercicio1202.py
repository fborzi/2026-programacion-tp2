# escribi un programa que solicite al usuario ingresar un número entero y luego determine si el número es mayor, menor o igual a 10.

entero = int(input("Ingrese un número entero: "))

if entero > 10:
    print("El número es mayor que 10.")
elif entero == 10:
    print("El número es igual a 10.")
else:
    print("El número es menor que 10.")
