numero1 = int(input("Ingrese primer numero entero:"))
numero2 = int(input("Ingrese segundo numero entero:"))
if numero1 > numero2:
    print(numero1, "es mayor que", numero2)
elif numero1 == numero2:
    print(numero1, "es igual a", numero2)
else:
    print(numero1, "es menor que", numero2)