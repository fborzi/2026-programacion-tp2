"""en este ejercicio se pide calcular e imprimir la suma de los 25 numeros de la sucesion de Fibonancci"""
numero1= 0
numero2= 1
suma = 0
for i in range(25):
    print(numero1)
    suma = suma + numero1
    siguiente = numero1 + numero2
    numero1 = numero2
    numero2 = siguiente
print(suma)