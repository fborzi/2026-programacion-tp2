num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

suma = num1 + num2
print("La suma de los dos numeros es:", suma)

resta = num1 - num2
print("La resta del primer numero menos el segundo es:", resta)

multiplicacion = num1 * num2
print("La multiplicacion de los dos numeros es:", multiplicacion)

if num2 == 0:
    print("No es posible realizar la division porque el divisor es 0")
    print("No es posible calcular el resto porque el divisor es 0")
    print("No es posible calcular la division entera porque el divisor es 0")
else:
    division = num1 / num2
    print("La division del primer numero entre el segundo es:", division)
    resto = num1 % num2
    print("El resto de la division del primer numero entre el segundo es:", resto)
    division_entera = num1 // num2
    print("La division entera del primer numero entre el segundo es:", division_entera)

print("El valor absoluto del primer numero es:", abs(num1))
print("El valor absoluto del segundo numero es:", abs(num2))
