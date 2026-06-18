"Escribir un programa que solicite al usuario dos números enteros y luego imprima la suma, resta, multiplicación, división, resto de la división, división entera y valor absoluto de ambos números."
entero1 = int(input("Ingrese el primer número entero: "))
entero2 = int(input("Ingrese el segundo número entero: "))

print("La suma de los dos numero es: ", entero1 + entero2)
print("La resta del primer numero menos el segundo es: ", entero1 - entero2)
print("La multiplicación de los dos numero es: ", entero1 * entero2)
if entero2 != 0:
    print("La division del primer numero entre el segundo es: ", entero1 / entero2)
else:    print("No se puede dividir por cero.")

print("El resto de la division del primer numero entre el segundo es:", entero1 % entero2)

if entero2 != 0:
    print("La division entera del primer numero entre el segundo es: ", entero1 // entero2)
else:    print("No se puede dividir por cero.")

print("El valor absoluto del primer numero es: ", abs(entero1))
print("El valor absoluto del segundo numero es: ", abs(entero2))