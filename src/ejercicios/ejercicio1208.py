"""Genera e imprime los primeros 25 numeros 
de la sucesion de Fibonacci"""
a = 0
b = 1

for i in range(25):
    print(a)
    siguiente = a + b
    a = b
    b = siguiente
