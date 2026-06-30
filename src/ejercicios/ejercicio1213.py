numero = 0
esPrimo = True
contador = 0

numero = int(input("Ingrese un numero entero mayor a 1:"))

while numero != 0 :
    if numero > 1 :
        for n in range (2, numero) :
            if numero % n == 0 :
                esPrimo= False
                break
            else :
                esPrimo = True
        if esPrimo : 
            contador = contador + 1
    else :
        print("El numero debe ser mayor a 1")
    numero = int(input("Ingrese un numero entero mayor a 1:"))
print("Cantidad de numeros primos ingresados:", contador)