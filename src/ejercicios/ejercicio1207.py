cantidadNumeros = int(input("Ingrese la cantidad de numeros que desea ingresar:"))
contador=0
pares = 0
impares = 0

while cantidadNumeros > contador:
    numero = int(input("Ingresa un numero"))
    contador= contador + 1
    if numero % 2 :
        pares = pares + 1
    else :
        impares =  impares + 1
print("La cantidad de numeros pares es:" , pares)
print("La cantidad de numeros impares es:" , impares)