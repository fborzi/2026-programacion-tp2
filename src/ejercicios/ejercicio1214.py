cadena=input("Ingrese una cadena de texto:")
palabrasTotal = cadena.strip().count(" ") + 1
letrasPalabra = 0
palabra = ""

print("La cantidad de palabras en la cadena es:", palabrasTotal)

for n in cadena + " ":
    if n != " " :
        palabra = palabra + n
        letrasPalabra = letrasPalabra + 1
    else:
        if letrasPalabra > 0: 
            print("La palabra",palabra,"tiene", letrasPalabra, "letras")
            letrasPalabra = 0  
            palabra=""

