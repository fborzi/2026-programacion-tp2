""" Modificar el programa anterior para que si ingresa un numero negativo, no se sume pero 
continue con el proceso. finalmente, mostrar por separado la suma de los numeros positivos 
pares o impares imgresados """


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


print(f"la suma total de los numeros ingresados: {acumulador_par}")
print(f"la suma total de los numeros ingresados: {acumulador_impar}")