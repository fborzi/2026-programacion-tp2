
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

print(f"La suma es: {suma}")
print(f"La resta es: {resta}")
print(f"La multiplicacion es: {multiplicacion}")

if num2 == 0:
    print("No se puede dividir por cero")
    print("No se puede dividir por cero")
    print("No se puede dividir por cero")
else:
    division = num1 / num2
    division_entera = num1 // num2
    resto = num1 % num2
    print(f"La division es: {division}")
    print(f"La division entera es: {division_entera}")
    print(f"El resto es: {resto}")

print(f"El valor absoluto es: {abs(num1)}") 