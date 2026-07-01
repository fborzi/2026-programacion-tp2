dia = input("Ingrese el día de la semana: ").lower()

cantidad = int(input("Ingrese la cantidad de artículos: "))

if dia == "lunes" and cantidad > 3:
    print("Accede al descuento")