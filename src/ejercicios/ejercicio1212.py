num = int(input("Ingrese un numero mayor que 1: "))
es_primo = True  
for i in range(2, num):
    if num % i == 0:
        es_primo = False
        break

if es_primo:
    print("El numero", num, "es PRIMO.")
else:
    print("El numero", num, "NO es primo.")
