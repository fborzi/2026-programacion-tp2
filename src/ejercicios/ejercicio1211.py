"""Este programa permite ingresar 20 números enteros comprendidos entre -10 y 10,
verificando que cada valor ingresado pertenezca al rango establecido. Durante
el proceso se calcula la suma de los números negativos, la cantidad de valores
iguales a cero y el promedio de los números positivos, mostrando finalmente
los resultados obtenidos."""

suma_negativos = 0
cantidad_ceros = 0
cantidad_positivos = 0
suma_positivos = 0
cantidad_fuera_rango = 0

for i in range(20):

    numero = int(input())

    while numero < -10 or numero > 10:
        cantidad_fuera_rango += 1
        numero = int(input())

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
    promedio = 0

for i in range(cantidad_fuera_rango):
    print("Numero fuera de rango. Intente nuevamente.")

print("La cantidad de numeros negativos es:", suma_negativos)
print("La cantidad de ceros es:", cantidad_ceros)
print("El promedio de los numeros positivos ingresados es:", promedio)