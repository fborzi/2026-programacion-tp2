"""Este programa solicita al usuario el dia de la semana y la cantidad de articulos
comprados por un cliente en una tienda, finalmente imorime 'accede al descuento'si
es dia lunes y el cliente compro mas de 3 articulos, de lo contrario no imprime nada"""

dia_semana=input("Ingrese el dia de la semana: ")
cantidad_articulos=int(input("Ingrese la cantidad de articulos comprados: "))

if dia_semana == "lunes" and cantidad_articulos > 3:
    print("accede al descuento")