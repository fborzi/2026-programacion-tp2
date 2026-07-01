suma = 0
resta = 0
multiplicacion = 0
division = 0
resto = 0
division_entera = 0
absoluto1 = 0
absoluto2 =0

num1 = int(input("ingrese el primer numero:"))
num2 = int(input("ingrese el segundo numero:"))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
absoluto1 = abs(num1)
absoluto2 = abs(num2)

print("La suma de los dos numeros es:", suma)
print("La resta del primer numero menos el segundo es:", resta)
print("La multiplicación de los dos numeros es:", multiplicacion)
print("La división del primer numero entre el segundo es:", division)
print("El resto de la división del primer numero entre el segundo es:", resto)
print("La división entera del primer numero entre el segundo es:", division_entera)
print("El valor absoluto del primer numero es:", absoluto1)
print("El valor absoluto del segundo numero es:", absoluto2)

if num2 != 0:
    division = num1 / num2
    resto = num1 % num2
    division_entera = num1 // num2
    print("La división del primer numero entre el segundo es:", division)
    print("El resto de la división del primer numero entre el segundo es:", resto)
    print("La división entera del primer numero entre el segundo es:", division_entera)

if num2 == 0:
    print(" No se puede dividir por cero")

