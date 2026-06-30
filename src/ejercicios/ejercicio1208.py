""" El programa genera los primeros 25 términos de la sucesión de Fibonacci, 
en la cual cada número se obtiene sumando los dos términos anteriores, comenzando con 0 y 1. 
A medida que calcula cada término, lo muestra por pantalla y lo agrega a una variable acumuladora. 
Al finalizar la generación de los 25 términos, el programa obtiene y muestra la suma total de todos 
los números de la sucesión calculados."""

a = 0
b = 1

for i in range(25):
    print(a)

    siguiente = a + b
    a = b
    b = siguiente

