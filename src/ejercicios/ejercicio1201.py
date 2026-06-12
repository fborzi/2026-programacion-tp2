"""Este programa solicita el ingreso de dos numeros enteros y muestra
el resultado de su suma,su resta,su multiplicacion,el cociente de la division
le resto de la division, la division entera entre ambas y el valor absoluto de ambos"""


num_1=int(input("Ingrese el primer numero entero: "))
num_2=int(input("Ingrese el segundo numero entero: "))


suma = num_1 + num_2
resta = num_1 - num_2
multiplicacion = num_1 * num_2
if num_2 != 0:
    cociente = num_1 / num_2
    resto = num_1 % num_2
    division_entera = num_1 // num_2
else:
    cociente = "No se puede dividir por cero" 
    resto = "No se puede dividir por cero"
    division_entera = "No se puede dividir por cero"
absoluto_1 = abs(num_1)
absoluto_2 = abs(num_2)


print("La suma de los dos numeros es: ",suma)
print("La resta del primer numero menos el segundo es: ",resta)
print("La multiplicacion de los dos numeros es: ",multiplicacion)
print("La division del primer numero entre el segundo es: ",cociente)
print("El resto de la division del primer numero entre el segundo es: ",resto)
print("La division entera del primer numero entre el segundo es: ",division_entera)
print("El valor absoluto del primer numero es: ",absoluto_1)
print("El valor absoluto del segundo numero es: ",absoluto_2)