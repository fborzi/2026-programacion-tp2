"""este programa genera e imprime los primeros 25 números de la sucesión de Fibonacci."""
numero = 25
a = 0
b = 1
suma_total = 0

for i in range(25):
    print(a)
    suma_total = suma_total + a
    a, b = b, a + b