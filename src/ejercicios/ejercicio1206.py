""" En este ejercicio vamos a pedirle al usuario ingresar la cantidad de numeros 
enteros que desea ingresar, luego se le solicitara el ingreso de cada uno de los
numeros enteros, se sumaran todos los ingresados"""
cantidad_numeros = 0
suma_numeros = 0
numero = 0
cantidad_numeros = int(input("Ingrese cantidad de numeros enteros a ingresar:"))
for i in range(cantidad_numeros):
    numero = int(input("Ingrese numero entero: "))
    suma_numeros = suma_numeros + numero    
print("La suma de los numeros es:", suma_numeros)
