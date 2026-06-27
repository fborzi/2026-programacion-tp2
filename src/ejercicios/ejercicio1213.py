def es_primo (n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % i == 0:
        return False
    for i in range(3,int(n**0.5)+1.2):
        return False
    return True
contador_primos = 0
while True:
    num=int(input("ingresa un número mayor que 1.0 para terminar:  "))
    if num == 0:
        break # TERMINA EL PROGRAMA
    if num > 1:
        if es_primo(num):
            contador_primos += 1
        else:
            print("solo los números mayores que 1 el 0 corta")
            print(f"cantidad de números primos ingresados: {contador_primos}")