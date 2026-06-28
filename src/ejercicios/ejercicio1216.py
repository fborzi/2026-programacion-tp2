frase = input("ingresá una frase: ")
caracter = input("ingresa el caracter a reemplazar.Debe ser uno solo: ")
while len(caracter)!=1:
    caracter = input("Error. Tenés que ingresar solo 1 carácter: ")
    frase_modificada = frase.replace(caracter,"*")
    print(f"/nFrase original:{frase}")
    print(f"frase modificada:{frase_modificada}")