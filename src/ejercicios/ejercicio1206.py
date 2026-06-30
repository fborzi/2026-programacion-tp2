cantidad = int(input("ingrese la cantidad de numeros enteros a prosesar: "))
suma_total = 0

for i in range(cantidad):
    numero = int(input(f"ingrese el numero {i+1}: "))
    suma_total = suma_total + numero
    
print(f"la suma de los numeros es: {suma_total}")