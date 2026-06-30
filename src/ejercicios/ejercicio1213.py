""" en este ejercicio pediremos el ingreso de numeros enteros mayores a 1 y corroboraremos si se trata de nuemros primos 
o no primos, mostraremos la cantidad de numeros primos ingresados"""
cantidad_primos = 0
numero = int(input("ingrese numero mayor a 1: "))
while numero != 0:
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo == True:
        cantidad_primos = cantidad_primos + 1
    numero = int(input("ingrese numero mayor a 1: "))
print("Cantidad de numeros primos ingresados:",cantidad_primos)