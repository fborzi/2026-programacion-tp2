cadena = input("Ingrese una cadena de texto: ")
caracter = input("Ingrese un caracter: ")
cadenaNueva = ""

if len(caracter) == 1 :
    for letra in cadena :
        if letra == caracter :
            letra = "*"
            cadenaNueva= cadenaNueva + letra
        else :
            cadenaNueva= cadenaNueva + letra
print(cadenaNueva)