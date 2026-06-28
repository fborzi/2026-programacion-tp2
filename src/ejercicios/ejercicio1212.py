"""
En este ejercicio se pide que se ingrese un numero mayor que 1.
Si el numero es divisible por si mismo o por uno,
en pantalla va a indicar que es un numero primo.
"""
numero = int(input("Ingrese un número mayor que 1: "))

es_primo = True

for i in range(2, numero):
    if numero % i == 0:
        es_primo = False
        break

if es_primo:
    print("El numero", numero, "es PRIMO.")
else:
    print("El numero", numero, "NO es PRIMO.")