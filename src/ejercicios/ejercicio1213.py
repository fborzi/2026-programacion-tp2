"""
En este ejercicio, se pide que se ingresen números y cuando se coloque cero,
se termina de leer los datos ingresados y va a buscar que número es primo;
arrojando la cantidad.
"""
cantidad_primos = 0

numero = int(input("Ingrese un número: "))

while numero != 0:
    es_primo = True

    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break

    if es_primo:
        cantidad_primos += 1

    numero = int(input("Ingrese un número: "))

print("Cantidad de numero primos ingresados:", cantidad_primos)
