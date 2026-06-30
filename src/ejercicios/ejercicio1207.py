# escribi un programa que solicita al usuario una cantidad de valores a ingresar,
# luego pide esos valores y muestra la suma de los números pares y la suma de los números impares ingresados.
cant = int(input("Ingrese la cantidad de valores que desea ingresar y luego ingrese los valores: "))

contadorpar = 0
contadorimpar = 0

for i in range(cant):
    valor = int(input(""))
    if valor % 2 == 0 and valor > 0:
        contadorpar = contadorpar + valor
    elif valor % 2 != 0 and valor > 0:
        contadorimpar = contadorimpar + valor

print("La suma de los números pares es:", contadorpar)
print("La suma de los números impares es:", contadorimpar)
