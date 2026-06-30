# escribi un programa que ingresa una serie de números y determine cuántos de ellos son primos.
# El programa debe continuar solicitando números hasta que el usuario ingrese 0, luego imprimir el total"

import math
contador = 0
numeros = int(input(""))

while numeros != 0:
    if numeros >= 2:
        es_primo = True
        for i in range(2, int(math.sqrt(numeros)) + 1):
            if numeros % i == 0:
                es_primo = False
                break

        if es_primo:
            contador += 1

    numeros = int(input(""))

print("Cantidad de numeros primos ingresados:", contador)
