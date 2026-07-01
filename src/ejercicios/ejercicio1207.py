"""
En el ejercicio 1207 pide que el usuario ingrese cierta cantidad de numeros y verifica si son pares o impares, en caso de ser negativo no se toma en cuenta 
Utilice una estructura repetitiva para que el usuario ingrese los numeros y destro de ella use una estructura condicional para que el sistema no cuente los numeros negativos y para 
identificar los numeros pares e impares para luego sumarlos. Por ultimo agregue un mensaje que le indica al usuario la suma de los numeros.


"""
cantidad= int(input("Ingrese cantidad de numeros: "))

suma_impares = 0
suma_pares = 0

for i in range(cantidad):
    num=int(input("Ingrese numero:"))

    if num < 0:
        continue
    if num % 2 == 0:
        suma_pares = num + suma_pares
    else:
        suma_impares = num + suma_impares
        
print("cantidad de numeros pares:",suma_pares)
print("cantidad de numeros impares:",suma_impares)


