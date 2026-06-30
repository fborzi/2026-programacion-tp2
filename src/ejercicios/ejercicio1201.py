num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))
suma = 0
resta = 0
resto = 0
division = 0.0
division_entera = 0


suma = num1 + num2
resta = num2 - num2
multiplicacion = num1 * num2
division = num1 / num2
division_entera = num1 // num2
absoluto1 = abs(num1)
absoluto2 = abs(num2)

if num2!= 0:
  division = num1 / num2
  resto = num1 % num2
  division_entera = num1 // num2


print("Mostrar la suma de los dos numeros:", suma)
print("Mostrar la resta del primero con el segundo:", resta)
print("La multiplicacion de los dos numeros: ", multiplicacion)
print("Resto de la division del primer numero con el segundo:", division)
print("el valor absoluto del primer numero:", absoluto1)
print("el valor absoluto del segundo numero:", absoluto2)