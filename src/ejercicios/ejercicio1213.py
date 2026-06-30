contador_primos = 0

num = int(input())

while num != 0:

    if num > 1:
        es_primo = True

        for i in range(2, num):
            if num % i == 0:
                es_primo = False
                break

        if es_primo:
            contador_primos += 1

    num = int(input())

print("cantidad de numeros primos ingresados:", contador_primos)
