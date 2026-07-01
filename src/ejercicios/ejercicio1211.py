"""
Ejercicio 1211 - Análisis de 20 números
Autor: Valentin Saldias
"""

suma_negativos = 0
cantidad_ceros = 0
cantidad_positivos = 0

for i in range(20):
    numero = int(input(f"Ingrese el número {i + 1}: "))

    if numero < 0:
        suma_negativos += numero
    elif numero == 0:
        cantidad_ceros += 1
    else:
        cantidad_positivos += 1

print("Suma fuera de rango:", suma_negativos)
print("Numero fuera de rango:", cantidad_ceros)
print("La cantidad de numeros positivos fueron:", cantidad_positivos)

if cantidad_positivos > 0:
    promedio = cantidad_positivos / 20
    print("El promedio de los numeros positivos ingresados es:", promedio)