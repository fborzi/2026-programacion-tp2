"""en este ejercicio se pide el ingreso de una cantidad indeterminada de numeros mayores a 1, finaliza
cuando se reciba 0 y mostrando la cantidad de numeros primos ingresados"""
cant_primos = 0
numero = int(input("Ingrese un numero mayor a 1: "))
while numero != 0:
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        cant_primos += 1
    numero = int(input("Ingrese un numero mayor a 1: "))
print("Cantidad de numeros primos ingresados:", cant_primos)
