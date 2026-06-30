numero = int(input("Ingrese un numero: "))

es_primo = True

if numero <= 1:
    es_primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False

if es_primo:
    print("El numero", numero, "es PRIMO.")
else:
    print("El numero", numero, "no es PRIMO.")
    