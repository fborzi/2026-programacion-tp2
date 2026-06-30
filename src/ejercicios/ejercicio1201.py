 num1 = int(input())
num2 = int(input())

print("la suma de los dos numeros es :", num1 + num2)
print("la resta del primer numero menos el segundo es:", num1 - num2)
print("la multiplicacion de los dos numeros es :", num1 * num2)

if num2 != 0:
    print("la division de los dos numeros es :", num1 / num2)
    print("la division entera entre ambos es :", num1 // num2)
    print("el resto de la division es :", num1 % num2)
else:
    print("No se puede dividir por cero")

print("el valor absoluto del primer numero es :", abs(num1))
print("el valor absoluto del segundo numero es :", abs(num2))                                                                  
