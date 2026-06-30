"""Este programa solicita la cantidad de números enteros a procesar y
permite ingresarlos uno por uno. Los valores negativos no se tienen en
cuenta en los cálculos, pero el proceso continúa normalmente. Al
finalizar, se muestra por separado la suma de los números positivos
pares y la suma de los números positivos impares ingresados."""

cantidad = int(input("Ingrese la cantidad de números enteros a procesar: "))

suma_pares = 0
suma_impares = 0

contador = 0


while contador < cantidad:
    numero = int(input())

    if numero < 0:
        continue

    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero

    contador += 1

print("Cantidad de numeros pares:", suma_pares)
print("Cantidad de numeros impares:", suma_impares)
