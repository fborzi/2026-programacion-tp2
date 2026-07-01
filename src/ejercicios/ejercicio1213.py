def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

contador_primos = 0
while True:
  num = int(input("Ingrese un numero mayor que 1 (0 para terminar): "))

  if num == 0:   
        break

  if es_primo(num):
        contador_primos += 1
print("Cantidad de numeros primos ingresados:", contador_primos)