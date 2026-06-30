a = 0
b = 1
suma = 0

for i in range(25):
    suma += a
    siguiente = a + b
    a = b
    b = siguiente

print("La suma de los primeros 25 números de Fibonacci es:", suma)