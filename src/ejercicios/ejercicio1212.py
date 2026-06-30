"""En este ejercicio pediremos al usuario ingresar un nymero mayor a 1 y le retornaremos si el mismo es
primo o no
"""
numero = 0
numero = int(input("ingrese numero mayor a 1: "))
es_primo = True
for i in range(2, numero):
    if numero % i == 0:
        es_primo = False
        break
if es_primo:
    print("El numero", numero, "es PRIMO.")
else:
    print("El numero", numero, "NO es PRIMO.")
