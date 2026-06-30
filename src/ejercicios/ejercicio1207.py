cantidad = int(input("ingrese la cantidad de numeros enteros a procesar: "))
suma_pares = 0
suma_impares = 0

for i in range(cantidad):
    numero = int(input("ingese el numero {i+1}:"))
    
    if numero < 0:
        if numero % 2 == 0:
            suma_pares = suma_pares + numero
        else:
            suma_impares = suma_impares + numero
            
print("cantidad de numeros pares: {suma_pares}")
print("cantidad de numeros impares: {suma_impares}")                