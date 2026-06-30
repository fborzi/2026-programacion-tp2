numero=input("ingrese un numero:")
numero1=input("ingrese otro numero:")
if int(numero)==int(numero1):
    print(numero, "es igual a ", numero1)
elif int(numero)>int(numero1):
    print(numero, "es mayor que ", numero1)
else:
    print(numero, "es menor que ", numero1)