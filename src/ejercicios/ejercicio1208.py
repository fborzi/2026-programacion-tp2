"""
Ejercicio 1208 - Sucesión de Fibonacci
Autor: Valentin Saldias
"""

n = int(input("Ingrese la cantidad de términos: "))

a = 0
b = 1

for i in range(n):
    print(a)
    siguiente = a + b
    a = b
    b = siguiente