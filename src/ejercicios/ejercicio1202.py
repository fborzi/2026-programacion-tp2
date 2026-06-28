"""
En este ejercicio vamos a ver si el numero que se ingresa
es mayor o menor que 10. Vamos a definir la variable, luego
pedimos que se ingrese un numero. En pantalla se mostrara
si el numero es mayor o menor.
"""

numero = 0
numero = int(input("Ingrese un numero: "))

if numero < 10:
    print("Menor que 10")
elif numero == 10:
    print("Igual a 10")
else:
    print("Mayor que 10")
    