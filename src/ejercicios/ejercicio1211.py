negativos = 0
ceros = 0
positivos = 0
suma_negativos = 0
suma_positivos = 0

contador = 0

while contador < 10:
    num = int(input())

    if num < -10 or num > 10:
        print("numero fuera de rango. intente nuevamente")
    else:
        contador += 1

        if num < 0:
            suma_negativos += num
            negativos += 1
        elif num == 0:
            ceros += 1
        else:
            suma_positivos += num
            positivos += 1

promedio = suma_positivos / positivos if positivos != 0 else 0

print("la cantidad de numeros negativos es:", suma_negativos)
print("la cantidad de ceros es:", ceros)
print("el promedio de los numeros positivos ingresados es:", promedio)
