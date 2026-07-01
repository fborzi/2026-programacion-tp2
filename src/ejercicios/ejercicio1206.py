"""
Ejercicio 1206 - Suma de números
Autor: Valentin Saldias
"""

cantidad = int(input("Ingrese la cantidad de números a procesar: "))

suma = 0

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    suma += numero

print("La suma de los numeros es:", suma)