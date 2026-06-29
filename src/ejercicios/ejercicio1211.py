suma_negativos = 0
contador_ceros = 0
suma_positivos = 0
contador_positivos = 0

for i in range(20):
    numero = int(input("ingrese un numero entre -10 y 10: "))
    
    if numero < -10 or numero > 10:
        print("numero fuera de rango. intente nuevamente.")
        numero = int(input("ingrese un numero entre -10 y 10: "))
        
    if numero < 0:
        suma_negativos = suma_negativos + numero
    elif numero == 0:
        contador_ceros = contador_ceros + 1
    else:
        suma_positivos = suma_positivos + numero
        contador_positivos = contador_positivos + 1
    
print("la cantidad de numero negativos es:", suma_negativos)
print("la cantidad de ceros es:", contador_ceros)

if contador_positivos > 0:
    promedio =suma_positivos / contador_positivos
else:                  
    promedio = 0
 
print("el promedio de los numeros positivos ingresados es:", promedio)              