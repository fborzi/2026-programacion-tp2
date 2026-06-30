dia = input("Ingrese el día de la semana: ")
cantidad = int(input("Ingrese la cantidad de artículos comprados: "))
if dia == "Lunes" and cantidad >= 5:
    print("Accedió al descuento.")
else:
    print("No accedió al descuento.")