cantidadNumeros = int(input("Ingrese la cantidad de numeros que desea ingresar:"))
contador=0
suma = 0

while cantidadNumeros > contador:
    suma = int(input("Ingresa un numero")) + suma 
    contador= contador + 1

print("La suma de todos los numeros es:", suma)