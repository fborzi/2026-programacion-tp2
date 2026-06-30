a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

suma = 0
resta = 0
division = 0.0
resto_division = 0
division_entera = 0

suma = a + b
resta = a - b
multiplicacion = a * b

if b !=0:
    division = a / b
    division_entera = a // b
    resto_division = a % b
else:
    print("No se puede dividir por cero")

print("La suma de los dos numeros es:", suma)
print("La resta del primer numero menos el segundo es:", resta)
print("La multiplicacion de los dos numeros es:", multiplicacion)
print("La division del primer numero entre el segundo es:", division)
print("El resto de la division del primer numero entre el segundo es:", resto_division)
print("La division entera del primer numero entre el segundo es:", division_entera)
print("El valor absoluto del primer numero es:", abs(a))
print("El valor absoluto del segundo numero es:", abs(b))