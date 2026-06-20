# pedir datos al usuario
dia = input("ingresa el día de la semana :").lower()
# para que el "lunes" = "lunes"
cantidad = int (input("ingresa la cantidad de articulos comprados:"))
# condicion lunes y mas de tres artícilos
if dia == "lunes" and cantidad > 3:
    print("accede al descuento")
     