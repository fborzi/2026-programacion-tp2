cadena = input("Ingrese una cadena de texto: ")
caracter = input("Ingrese un caracter: ")
cadenaNueva = ""

while len(caracter) != 1 :
    print("El caracter debe tener una logitud de 1")
    caracter = input("Ingrese un caracter: ")
   
if len(caracter) == 1: 
     for letra in cadena :
        if letra == caracter :
            letra = "*"
            cadenaNueva= cadenaNueva + letra
        else :
            cadenaNueva= cadenaNueva + letra
print(cadenaNueva)
