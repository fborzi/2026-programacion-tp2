"""En este ejercicio pediremos que ingrese caracteres que se concatenaran para formar una cadena hasta que ingresen
dos caracteres o el numero 0"""
cadena = ""
caracter = input("ingrese caracter: ")
while len(caracter) == 1 and caracter != "0":
    cadena += caracter
    caracter = input("ingrese caracter: ")
print(cadena)
