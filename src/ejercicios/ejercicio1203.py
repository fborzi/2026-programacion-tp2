"""Compara dos numeros."""
num1 = int(input("Escriba el numero 1:"))
num2 = int(input("Escriba el numero 2:"))
if num1 > num2:
    print(f"{num1} es mayor que {num2}.")
elif num1 < num2:
    print(f"{num1} es menor que {num2}.")
else:
    print(f"{num1} es igual a {num2}.")
