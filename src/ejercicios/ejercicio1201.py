num1 = int(input())
num2 = int(input())

print("la suma de los dos numeros es:", num1 + num2)
print("la resta de los dos numeros es:", num1 - num2)
print("la multiplicacion de los dos numeros es:", num1 * num2)

if num2 != 0:
    print("la division de los dos numeros es:", num1 / num2)
    print("la division entera de los numeros es:", num1 // num2)
    print("el resto de la division es:", num1 % num2)
else:
    print("no se puede dividir por cero")
