"Escribi un programa que solicite al usuario dos números enteros y luego imprima la suma, resta, multiplicación, división, resto de la división, división entera y valor absoluto de ambos números."
entero1 = int(input("Ingrese el primer número entero: "))
entero2 = int(input("Ingrese el segundo número entero: "))

suma = entero1 + entero2
resta = entero1 - entero2
multiplicacion = entero1 * entero2
division = entero1 / entero2 if entero2 != 0 else None
resto = entero1 % entero2 if entero2 != 0 else None
division_entera = entero1 // entero2 if entero2 != 0 else None

print("La suma de los dos numero es: ", suma)
print("La resta del primer numero menos el segundo es: ", resta)
print("La multiplicación de los dos numero es: ", multiplicacion)
if division is not None:
    print("La division del primer numero entre el segundo es: ", division)
else:
    print("No se puede dividir por cero.")

if resto is not None:
    print("El resto de la division del primer numero entre el segundo es:", resto)
else:
    print("No se puede calcular el resto.")

if division_entera is not None:
    print("La division entera del primer numero entre el segundo es: ", division_entera)
else:
    print("No se puede dividir por cero.")

print("El valor absoluto del primer numero es: ", abs(entero1))
print("El valor absoluto del segundo numero es: ", abs(entero2))
