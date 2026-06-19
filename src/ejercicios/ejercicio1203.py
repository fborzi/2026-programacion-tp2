"Escribir un programa que solicite al usuario ingresar dos números enteros y luego determine cuál de los dos números es mayor, o si son iguales. El programa debe mostrar un mensaje indicando el resultado."

X = int(input("Ingrese un número entero: "))
Y = int(input("Ingrese otro número entero: "))

if X > Y:
    print(X,"es mayor que", Y)
elif X == Y:
    print(X,"es igual a", Y)

else:
    print(X,"es menor que", Y)