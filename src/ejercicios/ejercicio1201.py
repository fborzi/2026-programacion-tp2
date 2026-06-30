""" en este ejercicio se realiza una suma, una resta, una division, multiplicacion, division y
division entera de 2 numeros enteros que se ingresan por teclado"""
suma = 0
resta = 0
division = 0.0
resto = 0
division_entera = 0
multiplicacion = 0
numero1 = int(input("Ingrese el primer numero entero: "))
numero2 = int(input("Ingrese el segundo numero entero: "))
if numero2 == 0:
    print("No se puede dividir por cero.")
else:
    suma = numero1 + numero2
    print("La suma de los dos numeros es:", suma)
    resta = numero1 - numero2
    print("La resta del primer numero menos el segundo es:", resta)
    multiplicacion = numero1 * numero2
    print("La multiplicacion de los dos numeros es:", multiplicacion)
    division = numero1 / numero2
    print("La division del primer numero entre el segundo es:", division)
    resto = numero1 % numero2
    print("El resto de la division del primer numero entre el segundo es:", resto)
    division_entera = numero1 // numero2
    print("La division entera del primer numero entre el segundo es:", division_entera)
    print("El valor absoluto del primer numero es:", abs(numero1))
    print("El valor absoluto del segundo numero es:", abs(numero2))
