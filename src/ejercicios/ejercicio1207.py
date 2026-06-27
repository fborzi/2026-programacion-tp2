cantidad = int(input())

suma_pares = 0
suma_impares = 0

for i in range(cantidad):
    numero = int(input())

    if numero < 0:
        continue

    if numero % 2 == 0:
        suma_pares = suma_pares + numero
    else:
        suma_impares = suma_impares + numero

print("Cantidad de numeros pares:", suma_pares)    
print("Cantidad de numeros impares:", suma_impares)