""" Solicito al usuario ingresar una frase e inicializo caracter y nueva_frase como strings vacios.
Utilizo un bucle while para validar que el usuario ingrese exactamente un caracter de longitud 1.
Recorro la frase letra por letra con un bucle for: si la letra actual es igual al caracter ingresado
la reemplazo por '*' y la acumulo en nueva_frase, sino acumulo la letra original.
Al finalizar muestro la nueva frase con todas las ocurrencias del caracter reemplazadas por '*' """

frase_ingresada = input("Ingresa una frase: ")
caracter = ""
nueva_frase = ""

while len(caracter) != 1:
    caracter = input("Ingrese un caracter: ")

for letra in frase_ingresada:
    if letra == caracter:
        nueva_frase = nueva_frase + "*"
    else:
        nueva_frase = nueva_frase + letra

print(nueva_frase)
