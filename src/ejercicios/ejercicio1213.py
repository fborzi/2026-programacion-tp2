numeros=int(input("ingresa un numero mayor a 0:"))
cantidadPrimos=0

while numeros!=0 and numeros>=0:
    primo=True
    for i in range(2,numeros):
        if numeros % i == 0:
            primo=False
            break

        if primo:
            cantidadPrimos+=1
    numeros=int(input("ingresa un numero mayor a 0:"))

print("la cantidad de numeros primos ingresadas es",cantidadPrimos )
