""" Este programa solicita el ingreso de dos números enteros y calcula
distintas operaciones entre ellos, como la suma, la resta, la multiplicación,
la división, el resto de la división, la división entera y el valor absoluto
de cada número, mostrando luego los resultados obtenidos en pantalla."""

a= int(input("Ingrese el primer numero: "))
b= int(input("Ingrese el segundo numero: "))

suma = 0
resta = 0
division = 0.0
resto = 0
division_entera = 0

suma = a + b
resta = a - b
multiplicacion = a * b
valor_absoluto_a = abs(a)
valor_absoluto_b = abs(b)

if b != 0:
    division = a / b
    resto = a % b
    division_entera = a // b
    
else:
    print("No se puede dividir por cero")

print ("La suma de los dos numeros es:", suma)
print ("La resta del primer numero menos el segundo es:", resta)
print ("la multiplicacion de los dos numeros es:", multiplicacion)
print ("La divison del primer numero entre el segundo es:", division) 
print ("El resto de la division del primer numero entre el segundo es:", resto)
print ("La division entera del primer numero entre el segundo es:", division_entera)
print ("El valor absoluto del primer numero es:", valor_absoluto_a)
print ("El valor absoluto del segundo numero es:", valor_absoluto_b)
