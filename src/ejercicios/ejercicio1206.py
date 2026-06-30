cantidad= int(input("Ingrese cantidad de numeros:"))

suma = 0 

for i in range(cantidad):
    num= int(input("Ingrese numero:"))
    suma = suma+num

print("La suma de los numeros es:", suma)