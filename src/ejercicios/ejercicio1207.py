"""Ignora numeros negativos y suma pares e impares por separado"""
cantidad = int(input("Ingrese la cantidad de numeros a procesar: "))
suma_pares = 0
suma_impares = 0
i = 0
while i < cantidad:
    numero = int(input())
    if numero < 0:
        continue

    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero
    i += 1
print("Cantidad de numero pares:", suma_pares)
print("Cantidad de numeros impares:", suma_impares)
