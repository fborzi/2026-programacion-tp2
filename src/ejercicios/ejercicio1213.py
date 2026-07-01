"""
Lee números hasta recibir 0 y cuenta cuántos son primos.
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
        cantidad_primos = cantidad_primos + 1

print(f"Cantidad de números primos ingresados: {cantidad_primos}")
