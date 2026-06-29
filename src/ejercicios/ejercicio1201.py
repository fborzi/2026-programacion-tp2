""" en este ejercicio se realiza una suma, una resta, una division, multiplicacion, division y
 division entera de 2 numeros enteros que se ingresan por teclado"""
suma = 0
resta = 0
division = 0.0
resto = 0
division_entera = 0
multiplicacion = 0

numero1 = int(input("ingrese primer numero entero: "))
numero2= int(input("ingrese un segundo numero entero: "))

suma = numero1 + numero2
print ("La suma de", numero1, "y", numero2, "es:", suma)

resta = numero1 - numero2
print ("La resta del primer numero", numero1, "menos" , numero2, "el segundo es:", resta)

multiplicacion = numero1 * numero2
print ("La multiplicacion de", numero1, "los dos numeros", numero2, "es:", multiplicacion)

if numero2 != 0: 
    division = numero1 / numero2
    print ("La division del primer numero", numero1, "entre el segundo", numero2, "es:", division)
else: 
    print("No se puede dividir por cero")

resto = numero1 % numero2
print ("")

division_entera = numero1 // numero2
print ("La division entera del primer numero", numero1, "entre el segundo es:", numero2)

print ("El valor absoluto del primer numero es:", abs(numero1))
print("El valor absoluto del segundo numero es:", abs(numero2))