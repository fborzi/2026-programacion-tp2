"""Este programa solicita al usuario el ingreso de una cantidad indeterminada
de números enteros mayores que 1, finalizando la carga cuando se ingresa
el valor cero. Para cada número ingresado, se verifica si es primo
analizando si tiene divisores distintos de 1 y de sí mismo. Se contabiliza
la cantidad total de números primos ingresados y, al finalizar el proceso,
se muestra dicho resultado."""

cant_primos = 0

num = int(input("Ingrese un numero mayor que 1 (0 para terminar): "))

while num != 0:

    while num <= 1:
        num = int(input("Ingrese un numero mayor que 1 (0 para terminar): "))

    es_primo = True

    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break

    if es_primo:
        cant_primos += 1

    num = int(input("Ingrese un numero mayor que 1 (0 para terminar): "))

print(f"Cantidad de numeros primos ingresados: {cant_primos}")
