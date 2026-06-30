"""Este programa solicita el ingreso de una cantidad de numeros indeterminadad 
mayores que 1, la carga finaliza cuando se ingresa el numero 0 y muestra
la cantidad de numeros primos ingresados"""

cantidad_primos = 0
numero = int(input("Ingrese un número mayor que 1 : "))

while numero != 0:

    if numero > 1:
        divisor = 2
        es_primo = True

        while divisor < numero and es_primo:
            if numero % divisor == 0:
                es_primo = False
            divisor += 1

        if es_primo:
            cantidad_primos += 1

    numero = int(input("Ingrese un número mayor que 1 (0 para finalizar): "))

print("Cantidad de números primos ingresados es:", cantidad_primos)