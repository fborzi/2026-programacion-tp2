suma_negativos = 0
cantidad_ceros = 0
suma_positivos = 0
cantidad_positivos = 0

for i in range(20):
    numero = int(input())

    while numero < -10 or numero > 10:
        print("Numero fuera de rango. Intente nuevamente.")
        numero = int(input())

    if numero < 0:
        suma_negativos = suma_negativos + numero
    elif numero == 0:
        cantidad_ceros = cantidad_ceros + 1
    else:
        suma_positivos = suma_positivos + numero
        cantidad_positivos = cantidad_positivos + 1
        
print(f"La suma de los numeros negativos es: {suma_negativos}")
print(f"La cantidad de ceros es: {cantidad_ceros}")

if cantidad_positivos > 0:
    promedio_positivos = suma_positivos / cantidad_positivos
else:
    promedio_positivos = 0.0

print(f"El promedio de los numeros positivos ingresados es: {promedio_positivos}")         