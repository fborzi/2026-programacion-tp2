"""Solicitar al usuario que ingrese el dia de la semana y la camtidad de articulos comprados 
por un cliente en una tienda. Finalmente, imprimir "accede al descuento " si el dia es lunes
y el cliente compro mas de tres articulos. en caso contrario no imprimir nada """

dia_semana = input("Ingrese el dia de la semana ").lower() 
articulos = int(input("Ingrese la cantidad de Articulos comprados "))

if dia_semana == ("lunes") and articulos > 3:
   print("accede al descuento ")
else :
   print("")