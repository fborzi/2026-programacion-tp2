"""Ejercicio 1214 - Analizar cadena de texto"""

cadena = input("Ingresá una cadena de texto: ")

contador_palabras = 0
longitud_palabra_actual = 0
palabra_actual = ""
resultado_detalles = ""

for caracter in cadena:
    if caracter != " ":
        palabra_actual += caracter
        longitud_palabra_actual += 1
    else:
        if longitud_palabra_actual > 0:
            contador_palabras += 1
            resultado_detalles += f"La palabra '{palabra_actual}' tiene {longitud_palabra_actual} letras.\n"
            palabra_actual = ""
            longitud_palabra_actual = 0

if longitud_palabra_actual > 0:
    contador_palabras += 1
    resultado_detalles += f"La palabra '{palabra_actual}' tiene {longitud_palabra_actual} letras.\n"

print(f"La cantidad de palabras en la cadena es: {contador_palabras}")
print(resultado_detalles, end="")