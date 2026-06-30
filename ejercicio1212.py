numero = int(input("Ingrese un número mayor que 1: "))

es_primo = True

for i in range(2, numero):
    if numero % i == 0:
        es_primo = False
        break

if es_primo:
    print("El número", numero, "es PRIMO.")
else:
    print("El número", numero, "NO es PRIMO.")