num1 = int(input())
num2 = int(input())

print("La suma de los dos numeros es:", num1 + num2)
print("La resta de el primer numero menos el segundo es:", num1 - num2)
print("La multiplicacion de los dos numeros es:", num1 * num2)

if num2 == 0:
    print("El numero 2 no se puede dividir porque es 0")
else: 
    print("La division del primer numero entre el segundo es:", num1 / num2)

print("El resto de la division del primer numero entre el segundo es:", num1 % num2)
print("La division entera del primer numero entre el segundo es:", num1 // num2)
print("El valor absoluto del primer numero es:", abs(num1))
print("El valor absoluto del segundo numero es:", abs(num2))