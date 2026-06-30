"""solicito dos numeros enteros y calculo suma, resta, multiplicacion y valor absoluto de ambos
que no dependen del segundo numero. si el segundo numero es cero informo el error al inicio
y en lugar de division, resto y division entera imprimo que no pudieron calcularse. si el
segundo numero es distinto de cero calculo e imprimo los tres resultados restantes."""

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
