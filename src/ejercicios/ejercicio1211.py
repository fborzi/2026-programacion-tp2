"""Escribi un programa que solicite el ingreso de 20 numeros enteros que se encuentren entre -10
y 10 e imprima la sumatoria de los valores negativos, la cantidad de valores iguales a cero y el
promedio de los valores positivos. Se debera pedir el reingreso de un numero si este estuviera
fuera del rango dado."""

numeros_enteros = 0
cantidad_cero = 0
suma_positivos = 0
suma_negativos = 0
total = 0

for i in range(20) :
    numeros_enteros = int(input("ingrese numero entero"))
    if numeros_enteros > -10 and numeros_enteros < 10 :
        if numeros_enteros < 0 :
            suma_negativos = suma_negativos + numeros_enteros
        elif numeros_enteros == 0 :
            cantidad_cero = cantidad_cero + 1
        else :
            numeros_enteros > 0 
            suma_positivos = suma_positivos + numeros_enteros
            total = total + 1
            promedio = suma_positivos / total
    else :
        print("Fuera de rango intente nuevamente")

print(f"la cantidad de numeros negativos es: {suma_negativos}")
print(f"la cantidad de ceros es: {cantidad_cero}")
print(f"el promedio de los numeros positivos ingresados es: {promedio}")
