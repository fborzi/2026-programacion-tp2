# Leer cantidad de números a procesar
cantidad = int(input("Ingrese la cantidad de números a procesar: "))

suma_pares = 0
suma_impares = 0

# Procesar los números ingresados
for i in range(cantidad):
    numero = int(input("Ingrese un número: "))
    # Ignorar números negativos
    if numero < 0:
        continue
    # Sumar según sea par o impar
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero

# Mostrar resultados
print("Suma de números pares:", suma_pares)
print("Suma de números impares:", suma_impares)