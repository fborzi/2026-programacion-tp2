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

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
resto = a % b
division_entera = a // b
absoluta_a = abs(a)
absoluta_b = abs(b)

print("La suma de los dos numeros es: ", suma)
print("La resta del primer numero menos el segundo es : ", resta)
print("La multiplicacion de los dos numeros es: ", multiplicacion)
print("La division del primer numero entre el segundo es: ", division)
print("El resto de la division del primer numero entre el segundo es: ", resto)
print("La division entera del primer numero entre el segundo es: ", division_entera)
print("El valor absoluto del primer numero es: ", absoluta_a)
print("El valor absoluto del segundo numero es: ", absoluta_b)
