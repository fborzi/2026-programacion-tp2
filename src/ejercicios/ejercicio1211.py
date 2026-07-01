sumatoria_negativos = 0
cantidad_ceros = 0
suma_positivos = 0
cantidad_positivos = 0

for i in range(20):
    num = int(input("Ingrese un numero entre -10 y 10: "))

    while num < -10 or num > 10:
        print("Numero fuera de rango. Intente nuevamente.")
        num = int(input("Ingrese un numero entre -10 y 10: "))

    if num < 0:
        sumatoria_negativos += num
    elif num == 0:
        cantidad_ceros += 1
    else:  # num > 0
        suma_positivos += num
        cantidad_positivos += 1

if cantidad_positivos > 0:
    promedio_positivos = suma_positivos / cantidad_positivos
else:
    promedio_positivos = 0
print("La sumatoria de los numeros negativos es:", sumatoria_negativos)
print("La cantidad de ceros es:", cantidad_ceros)
print("El promedio de los numeros positivos ingresados es:", promedio_positivos)
