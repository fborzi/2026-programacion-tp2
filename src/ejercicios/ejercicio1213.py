contador = 0

numero = int(input("Ingrese un numero: "))

while numero != 0:
    if numero > 1:
        es_primo = True

        for i in range(2, numero):
            if numero % i == 0:
                es_primo = False
        
        if es_primo:
            contador += 1
    numero = int(input("Ingrese un numero: "))
print("Cantidad de numero primos ingresados:", contador)