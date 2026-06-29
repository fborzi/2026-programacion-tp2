cantidad = int(input("cantidad de numeros enteros a procesar"))
suma_pares = 0
suma_impares = 0

for i in range(cantidad):
    num = int(input())
    
    if num > 0:
        if num % 2 == 0:
            suma_pares = suma_pares + num
        else:
            suma_impares = suma_pares + num
            
print("cantidad de numeros pares: " + str (suma_pares))
print("cantidad de numeros impares:" + str(suma_impares))                