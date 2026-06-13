numero1 = 0
numero2 = 0

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese un numero: "))

if numero1 > numero2:
    print(f"{numero1} es mayor que {numero2}.")
elif numero1 < numero2:
    print(f"{numero1} es menor que {numero2}.")
else:
    print(f"{numero1} es igual que {numero2}.")
    