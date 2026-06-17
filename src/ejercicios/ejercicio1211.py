cantidad = int(input("Ingrese la cantidad de numeros: "))

suma_negativos = 0
cantidad_ceros = 0
suma_positivos = 0
cantidad_positivos= 0
i = 0

while i < cantidad:
    numero = int(input("Ingrese un numero entre el -10 y 10: "))

    if numero < -10 or numero > 10:
        print("Numero fuera de rango. Intente nuevamente.")
    else:
        i += 1
    
        if numero < 0:
         suma_negativos += numero
        elif numero == 0:
            cantidad_ceros += 1
        else:
            suma_positivos += numero
            cantidad_positivos += 1
    

promedio = suma_positivos / cantidad
print("La suma de los numeros negativos es:", suma_negativos)
print("La cantidad de ceros es:", cantidad_ceros)
print("El promedio de los numeros positivos ingresados es:", promedio)