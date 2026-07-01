"""
Verifica si un número es primo probando divisibilidad desde 2 hasta n-1.
"""
numero = int(input("Ingrese un número para verificar si es primo:"))
es_primo = True

if numero < 2:
    es_primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break

if es_primo:
    print(f"El numero {numero} es primo.")
else:
    print(f"El numero {numero} no es primo.")
