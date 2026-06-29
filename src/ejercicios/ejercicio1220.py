"""solicito al usuario ingresar un texto y lo convierto a minusculas con .lower().
Solicito la cantidad de lugares que se correran las letras.
Defino el abecedario español de 27 letras como string para poder indexar cada letra.
Inicializo nueva_letra como string vacio para acumular el texto encriptado.
Recorro el texto letra por letra: si la letra esta en el abecedario calculo su posicion
con index(), le sumo el corrimiento y aplico %27 para que no se salga del abecedario como sugeriste, aunque el 
ejemplo esta mal porque lo hiciste con el abecedario en ingles(26 letras).
luego busco la nueva letra con esa posicion y la acumulo en nueva_letra.
Si el caracter no es una letra lo acumulo sin modificar.
Al finalizar imprimo el texto encriptado."""

texto = input("Ingresa el texto a encriptar: ").lower()
cantidad_lugares = int(input("Ingrese la cantidad de lugares que correran las letras "))
abecedario = "abcdefghijklmñnopqrstuvwxyz"
nueva_letra = ""
nueva_posicion = 0

for letra in texto:
    if letra in abecedario:
        posicion = abecedario.index(letra)
        nueva_posicion = (cantidad_lugares + posicion) % 27
        nueva_letra = nueva_letra + abecedario[nueva_posicion]
    else:
        nueva_letra = nueva_letra + letra
print(nueva_letra)
