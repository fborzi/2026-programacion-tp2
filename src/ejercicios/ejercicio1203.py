""" en este ejercicio se ingresan 2 numeros enteros y se comparan, mayor, menor o igual"""
x = int(input("Ingrese un numero entero: "))
y = int(input("Ingrese otro numero entero: "))
if x > y:
    print(x, "es mayor que", y)
else:
    if x < y:
        print(x, "es menor que", y)
    else:
        if x == y:
            print(x, "es igual a", y)
            