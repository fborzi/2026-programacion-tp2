"escribi un programa que lea 20 numeros enteros entre -10 y 10, y luego muestre la cantidad de numeros negativos, la cantidad de ceros y el promedio de los numeros positivos ingresados."

negativos = 0
igualcero = 0
positivos = 0
contadorpos = 0
contador = 0

while contador < 20:
    valores = int(input(""))
    if valores < -10 or valores > 10:
        print("Numero fuera de rango. Intente nuevamente.")
    elif valores < 0:
        negativos = negativos + valores
        contador += 1
    elif valores == 0:
        igualcero = igualcero + 1
        contador += 1
    else:
        positivos = positivos + valores
        contadorpos = contadorpos + 1
        contador += 1

print("La cantidad de numeros negativos es: ", negativos)
print("La cantidad de ceros es: ", igualcero)
print("El promedio de los numeros positivos ingresados es: ", positivos / contadorpos)
