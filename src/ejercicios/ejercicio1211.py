"""
Lee 20 números válidos entre -10 y 10 (repide si están fuera de rango)
y calcula suma de negativos, ceros y promedio de positivos.
"""
suma_negativos = 0
cantidad_ceros = 0
suma_positivos = 0
cantidad_positivos = 0
contador = 0

while contador < 20:
    numero = int(input())
    if numero < -10 or numero > 10:
        print("Numero fuera de rango. Intente nuevamente.")
        continue
    if numero < 0:
        suma_negativos = suma_negativos + numero
    elif numero == 0:
        cantidad_ceros = cantidad_ceros + 1
    else:
        suma_positivos = suma_positivos + numero
        cantidad_positivos = cantidad_positivos + 1
    contador += 1

promedio = suma_positivos / cantidad_positivos if cantidad_positivos > 0 else 0

print(f"La cantidad de numeros negativos es: {suma_negativos}")
print(f"La cantidad de ceros es: {cantidad_ceros}")
print(f"El promedio de los numeros positivos ingresados es: {promedio}")