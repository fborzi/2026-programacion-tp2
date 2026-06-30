suma_negativos = 0
cantidad_ceros = 0
suma_positivos = 0
cantidad_positivos = 0


for i in range(20):

    numero = int(input(f"Ingrese el número {i + 1}: "))


    while numero < -10 or numero > 10:
        print("Número fuera de rango. Intente nuevamente.")
        numero = int(input(f"Ingrese nuevamente el número {i + 1}: "))


    if numero < 0:
        suma_negativos += numero
    elif numero == 0:
        cantidad_ceros += 1
    else:
        suma_positivos += numero
        cantidad_positivos += 1

if cantidad_positivos > 0:
    promedio_positivos = suma_positivos / cantidad_positivos
else:
    promedio_positivos = 0

