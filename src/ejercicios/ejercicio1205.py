"""
El ejercicio 1205 pide que el usuario suba un dia a la semana y la cantidad de articulos comprados, si el dia es lunes y la cantidad de articulos es mas de 3, se le da un descuento 
utilice una estructura condicional para indicar si el usuario puede acceder al descuento o no y en cualquiera de los dos casos agregue un mensaje para indicar el resultado.

"""
dia = input("ingrese fecha:")
producto = int(input("Ingrese articulos comprados:"))

if dia == "lunes" and producto > 3:
    print("Accede al descuento")