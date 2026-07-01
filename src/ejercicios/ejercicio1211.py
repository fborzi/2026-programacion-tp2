"""En este ejercico pediremos el ingreso de 20 numeros que esten entre -10 y 10 de los cuales informaremos
si son datos esperados la suma de los numeros negativos, el promedio de los datos positivos y la cantidad
de 0 que se ingresaron, por lo contrario se informara 'valor fuera de rango' """
numero = 0
cantidad_ceros = 0
cantidad_positivos = 0
suma_positivos = 0
suma_negativos = 0
promedio = 0
for i in range(23):
    numero = int(input("ingrese numero entero entre -10 y 10: "))
    if numero > 10 or numero < -10:
        print("Numero fuera de rango")
    else:
        if numero == 0:
            cantidad_ceros = cantidad_ceros + 1
        if numero > 0:
            cantidad_positivos = cantidad_positivos + 1
            suma_positivos = suma_positivos + numero
        if numero < 0:
            suma_negativos = suma_negativos + numero
if cantidad_positivos > 0:
    promedio = suma_positivos / cantidad_positivos
else:
    promedio = 0 
print("La sumatoria de los valores negativos es:",suma_negativos)
print("La cantidad de ceros ingresados es:", cantidad_ceros)
print("El promedio de los valores positivos ingresados es:", promedio)
