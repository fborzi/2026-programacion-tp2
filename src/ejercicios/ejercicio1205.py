dia = input ("dia en el semana: ")
articulos = int(input("ingrese la cantidad de articulos comprados: "))

if dia == "lunes" and articulos > 3:
    print("accede al descuento.")
else:
    print("no accede al descuento.")