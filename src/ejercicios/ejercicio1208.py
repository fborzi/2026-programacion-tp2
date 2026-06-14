"""Este prorgama calcula la suma de los primeros 25 numeros de la suce
sion de Fibonacci"""


a = 1
b = 0
suma = 0
for i in range(25):
    suma = suma + a
    a , b = b, a + b
    print(a)