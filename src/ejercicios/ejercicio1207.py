"""Suma de positivos pares e impares este programa suma por separado los números positivos pares e impares"""
suma_pares = 0
suma_impares = 0

while True:
    numero = int(input())
    if numero == -1:
       break
    if numero > 0:
        if numero % 2 == 0:
            suma_pares = suma_pares + numero
        else:
            suma_impares = suma_impares + numero
            
print("cantidad de numeros pares:", suma_pares)
print("cantidad de numeros impares:", suma_impares)                