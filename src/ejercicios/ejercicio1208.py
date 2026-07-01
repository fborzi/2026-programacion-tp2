"""
El programa calcula e imprime la suma de los primeros
25 números de la sucesión de Fibonacci.
"""

a = 0
b = 1
suma = a + b

for i in range(23):
    c = a + b
    suma += c
    a = b
    b = c

print("La suma de los primeros 25 numeros de Fibonacci es:", suma)