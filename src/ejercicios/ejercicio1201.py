"""
Este programa pide el ingreso de dos numeros para mostrar la suma de ambos,
la resta del primer numero menos el segundo, la multiplicacion de ambos,
la division y division entera del primer numero sobre el segundo,
el resto de la division y el valor absoluto de ambos numeros.
"""
a = 0
b = 0
suma = 0
resta = 0
mult = 0
div = 0.0
resto = 0
div_e = 0
va_a = 0
va_b = 0
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
while b == 0 :
    print("El segundo numero no puede ser 0, ingrese el valor nuevamente")
    b = int(input("Ingrese el segundo numero: "))
suma = a + b
resta = a - b
mult = a * b
div = a / b
resto = a % b
div_e = a // b
va_a = abs(a)
va_b = abs(b)
print("La suma de los dos numeros es:",suma)
print("La resta del primer numero menos el segundo es:",resta)
print("La multiplicacion de los dos numeros es:",mult)
print("La division del primer numero entre el segundo es:",div )
print("El resto de la division del primer numero entre el segundo es:",resto)
print("La division entera del primer numero entre el segundo es:",div_e)
print("El valor absoluto del primer numero es:",va_a)
print("El valor absoluto del segundo numero es:",va_b)