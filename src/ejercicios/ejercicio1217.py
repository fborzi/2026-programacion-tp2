frase = ""
caracter = input("Ingresa un caracter:")

while len(caracter) == 1 and caracter != "0":
    frase = frase + caracter
    caracter = input("Ingresa un caracter:")
if frase != "" :
    print(frase)
else :
    print("No se ingreso ningun caracter valido")
