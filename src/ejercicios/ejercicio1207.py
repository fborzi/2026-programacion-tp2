cantidad=input("ingrese la cantidad de numeros:")
sumaPares=0
sumaImpares=0
for i in range(int(cantidad)):
    numero=input("ingrese un numero:")
    if int(numero)>=0:
        if int(numero)%2==0:
            sumaPares+= int(numero)
        else:
            sumaImpares+= int(numero)
print("la suma de los numeros pares es:", sumaPares)
print("la suma de los numeros impares es:", sumaImpares)
