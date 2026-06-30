cantidad = int(input("Ingrese la cantidad de numeros: "))

suma = 0

for i in range(cantidad):
    numero = int(input())
    suma = suma + numero

print("La suma de los numeros es:", suma)
