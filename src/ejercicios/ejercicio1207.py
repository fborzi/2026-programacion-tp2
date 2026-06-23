"""inicialice los acumuladores de pares e impares en cero. solicito la cantidad de numeros a procesar
y utilice un while que se repite esa cantidad de veces decrementando numeros en cada vuelta.
si el numero ingresado es positivo lo clasifico como par o impar usando el modulo 2 (es par si da 0) y lo sumo
al acumulador correspondiente, si es negativo simplemente lo ignoro y continua el proceso.
al finalizar imprimo por separado la suma de los positivos pares y la de los positivos impares."""


numeros = int(input("Ingrese la cantidad de numeros procesar "))
acumulador_par = 0
acumulador_impar = 0

while numeros != 0 :
    num_actual = int(input("Ingrese los numeros uno a uno "))
    if num_actual > 0 :
        if (num_actual % 2 ) == 0 :
            acumulador_par = acumulador_par + num_actual
        else : 
            acumulador_impar = acumulador_impar + num_actual
    numeros = numeros - 1

print(f"la suma total de los numeros pares ingresados: {acumulador_par}")
print(f"la suma total de los numeros impares ingresados: {acumulador_impar}")