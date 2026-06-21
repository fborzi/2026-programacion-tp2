suma = 0
resta = 0
division = 0.0
resto = 0 
division_entera = 0
multiplicacion = 0.0

nro1 = int(input("Ingrese el primer numero:"))
nro2 = int(input("Ingrese el segundo numero:"))

print("La suma de los dos numeros es:",nro1+nro2)
print("La resta del primer numero menos el segundo es:", nro1-nro2)
print("La multiplcacion de los dos numeros es:", nro1*nro2)
if nro2 != 0:
    print("La division del primer numero entre le segundo es:", nro1/nro2)
    print("El resto de la division del primer numero entre el segundo es:", nro1%nro2)
    print("La division entera del primer numero entre el segundo es:", nro1//nro2)
else:
    print("No se puede dividir por cero")
print("El valor absoluto del primer numero es:",abs(nro1))
print("El valor absoluto del segundo numero es:",abs(nro2))