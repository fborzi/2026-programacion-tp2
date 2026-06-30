"""en este ejercicio se debe ingresar por teclado un  numero mayor a 1 y determinar si es primo o no"""
numero = int(input("Ingrese un numero entero mayor a 1: "))
es_primo = True
for i in range(2, numero):
    if numero % i == 0:
        es_primo = False
        break
if es_primo:
    print("El numero", numero, "es primo.")
else:
    print("El numero", numero, "no es primo.")
