"""Ejercicio 1201 - Operaciones matemáticas básicas
Solicita el ingreso de dos números enteros e imprime el resultado de su
suma, resta, multiplicación, división, resto de la división, división
entera y el valor absoluto de cada uno. Si el segundo número es 0, no es
posible calcular la división (ni el resto ni la división entera, que
dependen de ella); en ese caso se informa el error como primera línea y
luego, en lugar de cada resultado que dependía de la división, se aclara
que no pudo calcularse, sin interrumpir el resto del programa. """

primer_numero = int(input("Ingrese el primer numero entero: "))
segundo_numero = int(input("Ingrese el segundo numero entero: "))

suma = primer_numero + segundo_numero
resta = primer_numero - segundo_numero
multiplicacion = primer_numero * segundo_numero
valor_absoluto_primero = abs(primer_numero)
valor_absoluto_segundo = abs(segundo_numero)

if segundo_numero == 0:
    print("No es posible calcular la division porque el segundo numero es cero")

print(f"La suma de los dos numeros es: {suma}")
print(f"La resta del primer numero menos el segundo es: {resta}")
print(f"La multiplicacion de los dos numeros es: {multiplicacion}")

if segundo_numero == 0:
    print("La division no pudo calcularse porque el segundo numero es cero")
    print("El resto de la division no pudo calcularse porque el segundo numero es cero")
    print("La division entera no pudo calcularse porque el segundo numero es cero")
else:
    division = primer_numero / segundo_numero
    resto_division = primer_numero % segundo_numero
    division_entera = primer_numero // segundo_numero
    print(f"La division del primer numero entre el segundo es: {division}")
    print(f"El resto de la division del primer numero entre el segundo es: {resto_division}")
    print(f"La division entera del primer numero entre el segundo es: {division_entera}")

print(f"El valor absoluto del primer numero es: {valor_absoluto_primero}")
print(f"El valor absoluto del segundo numero es: {valor_absoluto_segundo}")