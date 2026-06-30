negativos = 0
ceros = 0
positivos = 0
suma_pos = 0

for _ in range(10):
    n = int(input())

    while n < -10 or n > 10:
        print("numero fuera de rango. intente nuevamente")
        n = int(input())

    if n < 0:
        negativos += 1
    elif n == 0:
        ceros += 1
    else:
        positivos += 1
        suma_pos += n

promedio = suma_pos / positivos if positivos > 0 else 0

print("la cantidad de numeros negativos es:", negativos)
print("la cantidad de ceros es:", ceros)
print("el promedio de los numeros positivos ingresados es:", promedio)
