contador_primos = 0

for i in range(1000):
    numero = int(input("ingrese un numero mayor que 1. 0 para terminar: "))
    
    if numero == 0:
        break
    
    if numero > 1:
        es_primo = True
        for divisor in range(2, numero):
            if numero % divisor == 0:
                es_primo = False
                
        if es_primo == True:
            contador_primos = contador_primos + 1
            
print("cantidad de numeros primos ingresados:", contador_primos)       