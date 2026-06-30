cantidad_primos = 0


numero = int(input("Ingrese un número (0 para finalizar): "))

while numero != 0:

    if numero > 1:

        es_primo = True

        # Comprobar si tiene divisores
        for i in range(2, numero):
            if numero % i == 0:
                es_primo = False
                break

        if es_primo:
            cantidad_primos += 1

  
    numero = int(input("Ingrese un número (0 para finalizar): "))

