"""Este programa solicita al usuario la cantidad de números enteros que
desea ingresar y luego permite cargar cada uno de ellos. A medida que
se ingresan los valores, se calcula la suma total, mostrando el resultado
final una vez completado el proceso."""

cantidad = int(input("Ingrese la cantidad de números enteros a procesar: "))

suma = 0

for i in range(cantidad):
    numero = int(input())
    suma = suma + numero

print("La suma de los numeros es:", suma)
