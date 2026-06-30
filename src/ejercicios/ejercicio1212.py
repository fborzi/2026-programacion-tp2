# Escribi un programa que determine si un número ingresado por el usuario es primo o no.

import math

primo = int(input("Ingrese un número: "))

if primo < 2:
    print(f"El numero {primo} NO es primo.")
else:
    es_primo = True
    for i in range(2, int(math.sqrt(primo)) + 1):
        if primo % i == 0:
            es_primo = False
            break

    if es_primo:
        print(f"El numero {primo} es primo.")
    else:
        print(f"El numero {primo} no es primo.")
