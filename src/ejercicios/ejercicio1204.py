""" en este ejercicio pediremos el ingreso de un numero y calcularemos de forma matematica si el numero es par o
impar, luego imprimiremos el resultado"""
numero1 = int(input("Ingrese primer numero entero:"))
if numero1 % 2 == 0:
    print("El numero ",numero1, " es par")
else:
    print("El numero ",numero1, " es impar")