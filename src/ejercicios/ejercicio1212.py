numero = 0
esPrimo = True

numero = int(input("Ingrese un numero entero mayor a 1:"))

if numero > 1 :
    for n in range (2, numero) :
        if numero % n == 0 :
            esPrimo= False
            break
        else :
           esPrimo = True
    if esPrimo :
        print("El numero", numero, "es primo")
    else :
        print("El numero", numero, "No es primo")
else :
    print("El numero debe ser mayor a 1")