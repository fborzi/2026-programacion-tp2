""" Modifica el programa anterior para que ahora solicite el ingreso de dos numeros 
enteros y luego informe si el primero es mayor o no que el segundo, usando el formato
X es mayor que Y, sin ambos numeros son iguales deberia informar x igual a y"""

numeroX = int(input("Ingrese un numero entero: "))
numeroY = int(input("Ingrese un numero entero: "))

if numeroX > numeroY:
    print(numeroX , "es mayor que ", numeroY)
elif numeroX < numeroY:
   print(numeroX , "es menor que ", numeroY)
else:
    print(numeroX , "es igual a ", numeroY)
