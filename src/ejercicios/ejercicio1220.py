"""En este ejercicio perdiremos una cadena de caracteres para cifrarla por el metodo 'la cifra de cesar' en la 
cual mediante un alfabeto y un numero de corrimiento de lugares cifraremos una frase"""
texto = input("ingrese texto a encriptar: ").lower()
corrimiento = int(input("Ingrese numero de lugares: "))
alfabeto = "abcdefghijklmnñopqrstuvwxyz"
cadena = ""
for caracter in texto:
    if caracter in alfabeto:
        posicion = alfabeto.index(caracter)
        nueva_posicion = (posicion + corrimiento) % 27
        cadena += alfabeto[nueva_posicion]
    else:
        cadena += caracter
print(cadena)