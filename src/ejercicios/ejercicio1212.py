"""
Ejercicio 1212 - Verificar número primo
Autor: Valentin Saldias
"""

numero = int(input("Ingrese un número mayor que 1: "))

es_primo = True

for i in range(2, numero):
    if numero % i == 0:
        es_primo = False
        break

if es_primo:
    print("El numero SI es PRIMO.")
else:
    print("El numero NO es PRIMO.")