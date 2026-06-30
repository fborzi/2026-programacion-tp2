"""inicialice el acumulador en cero y solicito la cantidad de numeros a procesar.
utilice un while que se repite esa cantidad de veces, en cada vuelta solicito un numero
y lo sumo directamente al acumulador, luego decremento el contador. al finalizar imprimo
la suma total de los numeros ingresados."""

numeros = int(input("Ingrese la cantidad de numeros procesar "))
acumulador = 0

while numeros != 0 :
    acumulador = acumulador + int(input("Ingrese los numeros uno a uno "))
    numeros = numeros - 1
print(f"la suma total de los numeros ingresados: {acumulador}")
