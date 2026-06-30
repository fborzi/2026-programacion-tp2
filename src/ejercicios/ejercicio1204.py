"""ingresar un numero entero por teclado y se determinara si es par o impar"""
numero = int(input("Ingrese un numero entero:"))
if numero % 2 == 0:
    print("El numero", numero, "es PAR.")
else:
    print("El numero", numero, "es IMPAR.")
