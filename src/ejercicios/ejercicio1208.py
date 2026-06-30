# escribir un programa que muestre los primeros 25 números de la serie de Fibonacci


CANT = 23

a = 0
b = 1
fibo = 0

print("0")

for i in range(CANT):
    print(a + b)
    fibo = a + b
    a = b
    b = fibo
