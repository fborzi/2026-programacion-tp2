dia = input("ingrese fecha:")
producto = int(input("Ingrese articulos comprados:"))

if dia == "lunes" and producto > 3:
    print("Accede al descuento")
else:
    print("No accede al descuento")