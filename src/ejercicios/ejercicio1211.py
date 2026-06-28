"""
En este ejercicio se realiza el siguiente codigo en el cual, se pide que se ingrese
cierta cantidad de numero que solo esten entre un numero negativo y otro positivo.
Si el numero se encuentra fuera de ese rango, te avisa y te dice que ingreses otro 
numero que este dentro de lo que pide. Cuando finalice el ingreso de esos numero, el
codigo suma los negativos, la cantidad de ceros, los positivos y el promedio de los
numeros positivos.
"""
suma_negativos = 0
cantidad_ceros = 0
suma_positivos = 0
cantidad_positivos = 0

contador = 0

while contador < 20:
    numero = int(input("Ingrese un número entre -10 y 10: "))

    if numero < -10 or numero > 10:
        print("Numero fuera de rango. Intente nuevamente.")
    else:
        contador += 1

        if numero < 0:
            suma_negativos += numero
        elif numero == 0:
            cantidad_ceros += 1
        else:
            suma_positivos += numero
            cantidad_positivos += 1

if cantidad_positivos > 0:
    promedio = suma_positivos / cantidad_positivos
else:
    promedio = suma / cantidad

print("La cantidad de numero negativos es:", suma_negativos)
print("La cantidad de ceros es:", cantidad_ceros)
print("El promedio de los numeros positivos ingresados es:", promedio)