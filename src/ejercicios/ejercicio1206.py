"""Este programa solicita ingresar una cantidad de numeros enteros a procesar.
luego permite al usuario ir ingresando de a uno los numeros enteros,una vez finalizada la carga los suma"""

cantidad = int(input("Ingrese la cantidad de numeros a procesar: "))

suma = 0

for i in range(cantidad):
    numero = int(input())
    suma = suma + numero

print("La suma de los numeros es:", suma)