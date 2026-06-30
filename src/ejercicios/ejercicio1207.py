cantidad= int(input("Ingrese cantidad de numeros: "))

suma_impares = 0
suma_pares = 0

for i in range(cantidad):
    num=int(input("Ingrese numero:"))

    if num < 0:
        continue 

    if num %2 == 0:
        suma_pares = num+suma_pares

    else:
        suma_impares = num+suma_impares 
        
print("cantidad de numeros pares:",suma_pares)
print("cantidad de numeros impares:",suma_impares)


