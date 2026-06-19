num1 = int(input("Ingrese otro numero entero: "))
num2 = int(input("Ingrese otro numero entero: "))
suma=0
resta=0
division=0
multiplicacion=0
divisionEnt=0
valorAbsolutoA=abs(num1)
valorAbsolutoB=abs(num2)
resto=0

suma=num1+num2
resta=num1-num2
multiplicacion=num1*num2
division= num1/num2
divisionEnt= num1//num2
resto=num1%num2

print("La suma de los dos numeros es:", suma)
print("La resta del primeer numero y menos segundo es:", resta)
print("La multiplicacion de los dos numeros es:", multiplicacion)
print("La division del primero numero entre el segundo es:", division)
print("El resto de la division del primer numero entre el segundo es:", resto)
print("La division entera del primero numero entre el segundo es:", divisionEnt)
print("El valor absoluto del primer numero es:", valorAbsolutoA)
print("El valor absoluto del segundo numero es:", valorAbsolutoB)
