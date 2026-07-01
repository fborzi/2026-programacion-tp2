"""Operaciones basicas entre dos numeros."""
a = int(input("Escriba el primer numero: "))
b = int(input("Escriba el segundo numero: "))

if b == 0:
    print("Error: no se puede dividir por cero.")

print(f"La suma de los dos numeros es: {a + b}")
print(f"La resta del primer numero menos el segundo es: {a - b}")
print(f"La multiplicacion de los dos numeros es: {a * b}")

if b != 0:
    print(f"La division del primer numero entre el segundo es: {a / b}")
    print(f"El resto de la division del primer numero entre el segundo es: {a % b}")
    print(f"La division entera del primer numero entre el segundo es: {a // b}")
else:
    print("Error: no se puede calcular la division porque el divisor es cero.")
    print("Error: no se puede calcular el resto porque el divisor es cero.")
    print("Error: no se puede calcular la division entera porque el divisor es cero.")

print(f"El valor absoluto del primer numero es: {abs(a)}")
print(f"El valor absoluto del segundo numero es: {abs(b)}")