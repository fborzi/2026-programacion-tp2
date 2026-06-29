cantidad = int(input("cantidad de numeros enteros a prosesar"))
suma = 0

for i in range(cantidad):
    num = int(input())
    suma = suma + num
    
print("la suma de los numeros es: " + str(suma))