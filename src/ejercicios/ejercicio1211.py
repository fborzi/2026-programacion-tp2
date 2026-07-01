sumanegativos = 0
cantceros = 0
sumapositivos = 0

for i in range(20):
    num = int(input("Ingrese un número entre -10 y 10:"))

    while num < -10 or num > 10:
        print("Numero fuera de rango intente nuevamente")
        num = int(input("Ingrese un numero entre -10 y 10:"))
    
    if num <0:
        sumanegativos = sumanegativos + num 

    elif num == 0: 
        cantceros += 1

    else:
        suapositivos = sumapositivos + num 
    
    print("La cantidad de numeros negativos es:", sumanegativos)
    print("La cantidad de ceros es:", cantceros)
    print("El promedio de los numeros positivos ingresados es:", sumapositivos)


