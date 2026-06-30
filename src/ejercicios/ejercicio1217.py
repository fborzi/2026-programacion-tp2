resultado = ""

while True:
    caracter = input("Ingresá un carácter: ")
    
    if len(caracter) != 1 or caracter == "0":
        break
    
    resultado += caracter

print(resultado)