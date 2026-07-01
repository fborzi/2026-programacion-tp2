"""
El ejercicio 1206 solicita que el usuario ingrese cierta cantidad de numeros y los sume, por eso uso una estructura repetitiva para que el usuario
pueda ingresar los nueros y dentro de ella utilice una estructura condicional para que el sistema no cuente los numeros negativos.

"""
cantidad= int(input("Ingrese cantidad de numeros:"))

suma = 0 

for i in range(cantidad):
    num= int(input("Ingrese numero:"))
    suma = suma+num

print("La suma de los numeros es:", suma)