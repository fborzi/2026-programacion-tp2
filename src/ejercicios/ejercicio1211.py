"""en este ejercicio se pide el igreso de 20 numeros enteros que esten entre -10 y 10, que se sumen 
los negativos, se sumen los iguales a 0 y el promedio de los valores positivos. si hay un numero fuera 
del rango dado se pedira el reeingreso"""
suma_negativos = 0
suma_positivos = 0
cant_ceros = 0
cant_positivos = 0
contador = 0
while contador < 20:
    numero = int(input("Ingrese un numero entre -10 y 10: "))
    while numero < -10 or numero > 10:
        print("Numero fuera de rango. Intente nuevamente.")
        numero = int(input("Ingrese un numero entre -10 y 10: "))

    if numero < 0:
        suma_negativos += numero
    elif numero == 0:
        cant_ceros += 1
    else:
        suma_positivos += numero
        cant_positivos += 1
    contador += 1
if cant_positivos > 0:
    promedio = suma_positivos / 20
else:
    promedio = 0
print("La cantidad de numeros negativos es:", suma_negativos)
print("La cantidad de ceros es:", cant_ceros)
print("El promedio de los numeros positivos ingresados es:", promedio)
