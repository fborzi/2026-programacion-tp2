cantidad = int(input())

pares = 0
impares = 0

for _ in range(cantidad):
    numero = int(input())

    if numero < 0:
        continue

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("cantidad de numeros pares:", pares)
print("cantidad de numeros impares:", impares)
