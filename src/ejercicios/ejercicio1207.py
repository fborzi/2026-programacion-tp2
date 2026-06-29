""" En este ejercicio vamos a modificar el ejercicio anterior """
cantidad_numeros = 0
suma_numeros_pares = 0
suma_numeros_impares = 0
numero = 0
cantidad_numeros = int(input("Ingrese cantidad de numeros enteros a ingresar:"))
for i in range(cantidad_numeros):
    numero = int(input("Ingrese numero entero: "))
    if numero > 0:
        if numero % 2 == 0:
            suma_numeros_pares = suma_numeros_pares + numero
        else:
            suma_numeros_impares = suma_numeros_impares + numero
print("La suma de los numeros par es:", suma_numeros_pares)
print("La suma de los numeros impar es:", suma_numeros_impares)
    