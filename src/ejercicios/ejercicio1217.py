resultado = ""
while True:
    caracter = input("Ingrese un caracter (0 para terminar): ")

    
    if caracter == "0" or len(caracter) != 1:
        break

    
    resultado += caracter
print("El string formado es:", resultado)