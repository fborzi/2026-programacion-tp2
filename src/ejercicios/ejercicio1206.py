"""
En este ejercicio se pide la cantidad de numeros que se quieran sumar, si se ingresa
por ejemplo el numero 6, luego se procede a ingresar numero por numero para que luego 
se sumen esos 6 numero ingresados arrojando el resultado.
"""
cantidad = int(input("Ingrese la cantidad de números a procesar: "))

suma = 0

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    suma = suma + numero

print("La suma de los números es:")
print(suma)
