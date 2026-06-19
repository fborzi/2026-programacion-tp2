"""
EN ESTE EJERCICIO PEDIMOS QUE SE IINGRESE UN NUMERO, PARA VERIFICAR SI 
ESE NUMERO ES PAR O IMPAR SOLO SI AL DIVIDIRLO POR DOS DA 0.
"""
numero = int(input("Ingrese un numero entero: "))

if numero % 2 == 0:
    print(f"El numero {numero} es PAR")
else:
    print(f"El numero {numero} es IMPAR")
