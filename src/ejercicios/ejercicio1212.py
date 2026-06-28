"Escribi un programa que determine si un número ingresado por el usuario es primo o no. Un número primo es aquel que solo es divisible por 1 y por sí mismo."

import math

primo = int(input("Ingrese un número: "))

if primo < 2:
    print("no es primo")
else:
    es_primo = True
    for i in range(2, int(math.sqrt(primo)) + 1):
        if primo % i == 0:
            es_primo = False
            break

    if es_primo:
        print("es primo")
    else:
        print("no es primo")
