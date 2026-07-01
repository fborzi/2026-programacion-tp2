"""
Ignora los negativos y separa la suma en pares e impares.
"""
cantidad = int(input("Ingrese la cantidad de numeros a ingresar:"))
suma_pares = 0
suma_impares = 0
i = 0

for i in range(cantidad):
    numero = int(input("Ingrese un numero:"))
    if numero < 0:
        continue
    if numero % 2 == 0:
        suma_pares = suma_pares + numero
    else:
        suma_impares = suma_impares + numero

print(f"Cantidad de numeros pares: {suma_pares}")
print(f"Cantidad de numeros impares: {suma_impares}")
