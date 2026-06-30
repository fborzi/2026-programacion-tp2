cantidad=input("ingrese la cantidad de numeros:")
suma=0
for i in range(int(cantidad)):
    numero=input("ingrese un numero:")
    suma += int(numero)

print("la suma de los numeros es:", suma)