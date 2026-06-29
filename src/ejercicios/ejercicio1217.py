"""en este ejercicio pide ingresar caracteres de longuitud 1, de a uno, finaliza la repeticion cuando
se ingrese un caracter que no tenga longuitud 1 o cuando se ingrese un numero. cuando finalice
que se muestre completo lo que se formo con los caracteres ingresados """
cadena = ""
caracter = input("Ingrese un caracter: ")
while len(caracter) == 1 and caracter != "0":
    cadena += caracter
    caracter = input("Ingrese un caracter: ")
print(cadena)
