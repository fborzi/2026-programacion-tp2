# escribi un programa que pida al usuario la cantidad de valores que desea ingresar,
# luego pide esa cantidad de valores y finalmente muestra la suma de todos ellos."
cant = int(input("Ingrese la cantidad de valores que desea ingresar y luego ingrese los valores: "))

contador = 0

for i in range(cant):
    valor = int(input(""))
    contador = contador + valor
print("La suma de los valores ingresados es: ", contador)
