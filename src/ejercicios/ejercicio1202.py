""" Se solicita un numero entero al usuario, convirtiendo directamente el texto
ingresado a tipo int. Luego se compara contra 10 e informa si es mayor o menor. """

numero_entero = int(input("Ingrese un numero entero: "))

if numero_entero > 10:
    print("El numero ingresado es mayor que 10")
else:
    print("El numero ingresado es menor o igual que 10")
