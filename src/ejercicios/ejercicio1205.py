"""solicito el dia de la semana convirtiendolo a minusculas para evitar problemas con mayusculas,
y la cantidad de articulos comprados. si el dia es lunes y se compraron mas de tres articulos
imprimo que el cliente accede al descuento, en caso contrario no imprimo nada."""

dia_semana = input("Ingrese el dia de la semana: ").lower()
articulos = int(input("Ingrese la cantidad de Articulos comprados: "))

if dia_semana == ("lunes") and articulos > 3:
   print("accede al descuento.")
else:
   print("")
