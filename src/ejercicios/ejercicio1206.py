"""
Pide una cantidad de números y los va sumando uno por uno.
"""
cantidad = int(input("Ingrese cantidad de números a ingresar:"))
suma = 0
i = 0

for i in range(cantidad):
    numero = int(input(f"Ingrese el {i + 1} número:"))
    suma = suma + numero

print(f"La suma de los numeros es: {suma}")