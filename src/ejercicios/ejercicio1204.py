"""Este programa solicita el ingreso de un numero entero y imprmir
si es par o impar"""

num=int(input("Ingrese un numero entero: "))

if num % 2 == 0:
    print("El numero ",num," es PAR")
else:
    print("El numero ",num," es IMPAR")