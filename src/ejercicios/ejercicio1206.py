cantidad = int(input("¿Cuantos numeros desea ingresar? "))
suma = 0
for i in range(cantidad):
    numero = int(input(f"Ingrese el numero {i+1}: "))
    suma += numero  
print("La suma de los numeros es:", suma)
