"""
Este ejercicio es igual que el anterior (1206), solamente que al ingresa los numeros solo suma
los pares y los impares por otro lado. Si se llegara a ingresa un numero negativo, no lo suma.
"""
cantidad = int(input("Ingrese la cantidad de números a procesar: "))

suma_pares = 0
suma_impares = 0

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}: "))

    if numero < 0:
        continue

    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero

print("Cantidad numero pares:", suma_pares)
print("Cantidad de numero impares:", suma_impares)
