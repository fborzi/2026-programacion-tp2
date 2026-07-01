frase = ""

while True:
    caracter = input("Ingrese un caracter: ")
    
    if caracter == "0" or len(caracter) != 1:
        break
    frase = frase + caracter
print(frase)
