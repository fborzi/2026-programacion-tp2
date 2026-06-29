"""suma de 2 numeros,pde 2 valores y muentra su suma"""

num1 = int(input("ingrese el primer numero:"))
num2 = int(input("ingrese el segundo numero:"))

suma = 0
resta = 0
multplicacion = 0
divison = 0
resto = 0
division_entera = 0
valor_absoluto1 = 0
valor_absoluto2 = 0

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

print("la resta de dos numeros es:", num1 - num2)
print("la multiplicacion de dos numeros es:", num1 * num2)

if num2 == 0:
    print("la divison del primer numero entre el segundo es: cero no es divisible")
    print("la division entera del primer numero entre el segundo numero es:cero no es divible")
else:
    print("la division del primer numero entre el segundo es:", num1/ num2)  
    print("la division entera del primer numero entre el segundo es:", division_entera)
    print("el resto de la disivion es:", num1 % num2)
    
print("el valor absoluto del primer numero es:", abs(num1))
print("el valor absoluto del segundo numero es:", abs(num2))