"""en este ejercicio se pide ingresar una cantidad de numeros a procesar y luego permitir que el usuario
ingrese 1 a 1 la cantidad de numeros pedida, luego se debera mostrar la suma de todos los numeros"""
suma = 0
numeros = int(input("Ingrese la cantidad de numeros: "))
for i in range(numeros):
    numero = int(input("Ingrese un numero: "))
    suma = suma + numero
print("La suma de los numeros es:", suma)
