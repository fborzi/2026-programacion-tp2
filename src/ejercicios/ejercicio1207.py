cantidad = int(input("¿Cuantos numeros desea ingresar? "))
suma_pares = 0
suma_impares = 0
for i in range(cantidad):
    numero = int(input(f"Ingrese el numero {i+1}: "))
    
    if numero < 0:
        continue
    
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero
print("Suma de numeros pares:", suma_pares)
print("Suma de numeros impares:", suma_impares)