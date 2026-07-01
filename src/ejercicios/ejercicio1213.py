"""
Ejercicio 1213 - Contar números primos
Autor: Valentin Saldias
"""

cantidad_primos = 0

while True:
    numero = int(input("Ingrese un número (0 para finalizar): "))

    if numero == 0:
        break

    es_primo = True

    if numero < 2:
        es_primo = False
    else:
        for i in range(2, numero):
            if numero % i == 0:
                es_primo = False
                break

    if es_primo:
        cantidad_primos += 1

print("Cantidad de numeros primos ingresados:", cantidad_primos)