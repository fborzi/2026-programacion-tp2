"""solicito dos numeros enteros y los comparo, si el primero es mayor imprimo que X es mayor que Y,
si es menor imprimo que X es menor que Y, y si son iguales imprimo que X es igual a Y."""
numeroX = int(input("Ingrese un numero entero: "))
numeroY = int(input("Ingrese un numero entero: "))

if numeroX > numeroY:
    print(numeroX , "es mayor que ", numeroY)
elif numeroX < numeroY:
   print(numeroX , "es menor que ", numeroY)
else:
    print(numeroX , "es igual a ", numeroY)
