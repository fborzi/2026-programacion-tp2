"""en este ejercicio se pide modificar el ejercicio anterior para que si el usuario ingresa un numero
negativo no se sume pero que continue el proceso, luego mostrar por separado la suma de los numeros
positivos pares e impares que se ingresen"""
suma_numpares = 0
suma_numimpares = 0
numeros = int(input("Ingrese la cantidad de numeros: "))
contador = 0
while contador < numeros:
    numero = int(input("Ingrese un numero: "))

    if numero >= 0:
        if numero % 2 == 0:
            suma_numpares += numero
        else:
            suma_numimpares += numero
    contador += 1
print("Cantidad de numeros pares:", suma_numpares)
print("Cantidad de numeros impares:", suma_numimpares)
