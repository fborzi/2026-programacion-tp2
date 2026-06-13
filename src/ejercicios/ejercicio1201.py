"""
En el primer ejercicio vamos a solicitar que se ingresen dos numeros. 
Para ello antes vamos a definir las variables, despues vamos a definir
las constantes de cada uno. Y terminamos mostramos en pantalla los
resultados de cada uno.
"""
suma = 0
resta = 0
multiplicacion = 0
division = 0.0
resto = 0
division_entera = 0
absoluto_a = 0
absoluto_b = 0

a = int(input("Ingrese numero: "))
b = int(input("Ingrese numero: "))

SUMA = a + b
RESTA = a - b
MULTIPLICACION = a * b
DIVISION = a / b
RESTO = a % b
DIVISION_ENTERA = a // b
ABSOLUTO_A = abs(a)
ABSOLUTO_B = abs(b)

print("La suma de los dos numeros es: ", SUMA)
print("La resta del primer numero menos el segundo es : ", RESTA)
print("La multiplicacion de los dos numeros es: ", MULTIPLICACION)
print("La division del primer numero entre el segundo es: ", DIVISION)
print("El resto de la division del primer numero entre el segundo es: ", RESTO)
print("La division entera del primer numero entre el segundo es: ", DIVISION_ENTERA)
print("El valor absoluto del primer numero es: ", ABSOLUTO_A)
print("El valor absoluto del segundo numero es: ", ABSOLUTO_B)
