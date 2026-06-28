"Escribi un programa que determine si un número ingresado por el usuario es primo o no. Un número primo es aquel que solo es divisible por 1 y por sí mismo."

import math

primo = int(input("Ingrese un número: "))
if primo < 2:
    print(f"{primo} no es un número primo.")
else:
    for i in range(2, int(math.sqrt(primo)) + 1):
        if primo % i == 0:
            print(f"{primo} no es un número primo.")
            break
    else:
        print(f"{primo} es un número primo.")
