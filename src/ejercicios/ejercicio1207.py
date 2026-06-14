"""Este programa es como el anterior,pero si se ingresa un numero negativo no se sume
pero continue con el proceso ,finalmente mostrar los numeros positivos ingresados entre pares y impares"""

cantidad = int(input("Ingrese la cantidad de numeros a procesar: "))

suma = 0
suma_par = 0
suma_impar = 0

for i in range(cantidad):
    numero = int(input())
    if numero > 0:
        suma = suma + numero
        if numero % 2 == 0:
            suma_par = suma_par + numero
        else:
            suma_impar = suma_impar + numero



print("Cantidad de numeros pares:", suma_par)
print("Cantidad de numeros impares:", suma_impar)