"""Ingrese un programa que solicite ingresar una cantidad de numeros enteros a procesar
Luego, permitir al usuario ir ingresando uno a uno la cnatidad pedida de numeros. una vez 
finalizado el ingreso, se debera mostrar la suma total de los numeros ingresados """

numeros = int(input("Ingrese la cantidad de numeros procesar "))
acumulador = 0

while numeros != 0 :
    acumulador = acumulador + int(input("Ingrese los numeros uno a uno "))
    numeros = numeros - 1

print(f"la suma total de los numeros ingresados: {acumulador}")
