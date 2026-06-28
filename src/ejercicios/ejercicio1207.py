cantidad = int (input("ingresa la cantidad de números a procesar: "))
suma_pares = 0
suma_impares = 0
for i in range(cantidad):
    num= int(input(f"ingresa el numero {i+1}: "))
    if num <0:
        print("número negativo , se ignora.")
        continue # salta a siguiente ,no suma nada 
    if num % 2== 0:
        suma_pares += num # es par 
    else:
        suma_pares +=num # es inpar
        print("n---resultados----")
        print(f"suma de números pares positivos:{suma_pares}")
        print(f"suma de números impares positivos:{suma_impares}")