# pedir cuantos númros va a ingresar 
cantidad=int(input("ingresa la cantidad de números enteros a procesar:"))
# indicar la suma de en 0
suma-total = 0
# bucle para pedir cada número y sumarlo
for i in range(1,cantidad + 1):
    num=int(input(f"ingresa el nímero{i}:"))
    suma_total += num
    # es lo mismo que sum_total = sum_total + num
    
    # mostrar el resultado
print(f"la suma total de los números es ingresados es :{suma_total}")

    