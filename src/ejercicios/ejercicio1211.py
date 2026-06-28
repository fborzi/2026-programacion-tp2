suma_negativos = 0
cantidad_ceros = 0
suma_positivos = 0
cantidad_positivos= 0
for i in range (20):
    while True:
        num = int(input(f"ingresá el número {i+1}/20, entre -10 y 10: "))
        if -10 <= num <= 10:
            break # salgo del while 
        else:
            print("Error: El número debe estar entre -10 y 10. Reingresá.")
            # Clasifico el número
            if num <0:
                suma_negativos += num
            elif num == 0:
                cantidad_ceros += 1
            else: suma_positivos +=num
            cantidad_positivos += 1
            if cantidad_positivos > 0:
                promedio_positivos = suma_positivos / cantidad_positivos
            else:
                promedio_positivos = 0 # si no hubo positivos 
                print("/n---Resultados---")
                print(f"Sumatoria de valores negativos:{suma_negativos}")
                print(f"cantidad de valores iguales a cero:{cantidad_ceros}")
                print(f"promedio de valores positivos{promedio_positivos:.2f}")
                
