numero=int(input("ingrese un numero:"))
esPrimo=True

for i in range(2,numero):
    if numero % i == 0:
        esPrimo=False
        break
if esPrimo:
    print("el numero es primo")
else:
    print("el numero no es primo")