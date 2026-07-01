"""
Ejercicio 1207 - Suma de positivos pares e impares
Autor: Valentin Saldias
"""

cantidad = int(input("Ingrese la cantidad de números a procesar: "))

pares = 0
impares = 0

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}: "))

    if numero >= 0:
        if numero % 2 == 0:
            pares += numero
        else:
            impares += numero

print("Cantidad de numeros pares:", pares)
print("Cantidad de numeros impares:", impares)