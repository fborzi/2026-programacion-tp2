# Solicitar la cantidad de números a procesar
cantidad = int(input("Ingrese la cantidad de números a procesar: "))
# Inicializar la suma
suma = 0
# Ingresar los números y sumarlos
for i in range(cantidad):
    numero = int(input("Ingrese un número entero: "))
    suma = suma + numero
# Mostrar el resultado
print("La suma total de los números ingresados es:", suma)Leer numero entero