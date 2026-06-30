negativos = 0
positivos = 0
ceros = 0
sumaPositivos = 0

for i in range(20):
    numero = int(input("Ingrese un numero entero: "))

    while numero < -10 or numero > 10:
        print("Numero fuera de rango. Ingrese uno nuevo.")
        numero = int(input("Ingrese un numero entero: "))

    if numero < 0:
        negativos += numero
    elif numero == 0:
        ceros += 1
    else:
        sumaPositivos += numero
        positivos += 1

if positivos > 0:
    promedio = sumaPositivos / positivos
else:
    promedio = 0

print("La cantidad de numeros negativos es:", negativos)
print("La cantidad de ceros es:", ceros)
print("El promedio de los numeros positivos es:", promedio)