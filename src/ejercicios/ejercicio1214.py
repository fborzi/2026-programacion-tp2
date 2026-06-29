"""
Solicito al usuario ingresar una cadena de texto y elimino los espacios del inicio y final con .strip().
Inicializo cantidad_palabras en 1 para contar la primera palabra, que no tiene espacio antes y no seria
contada por el bucle. Inicializo letras en 0 para contar los caracteres de cada palabra. Inicializo
palabra como string vacio para ir acumulando las letras de cada palabra mientras no encuentre un espacio.

Primer bucle: recorro la cadena contando los espacios para obtener la cantidad total de palabras
y la imprimo antes de mostrar el detalle.

Segundo bucle: recorro la cadena letra por letra. Si encuentro un espacio, imprimo la palabra
acumulada con su cantidad de letras y reseteo letras y palabra para la proxima.
Si no encuentro un espacio, sumo 1 a letras y acumulo la letra en palabra.
Al terminar el bucle, imprimo la ultima palabra que no termina en espacio.
"""

cadena = input("Ingrese una cadena de texto: ").strip()
cantidad_palabras = 1
cantidad_letras = 0
palabra = ""

for letra in cadena:
    if letra == " ":
        cantidad_palabras = cantidad_palabras + 1
print(f"La cantidad de palabras en la cadena es: {cantidad_palabras} ")

for letra in cadena:
    if letra == " ":
        print(f"la palabra '{palabra}' tiene {cantidad_letras} letras.")
        cantidad_letras = 0
        palabra = ""
    else:
        cantidad_letras = cantidad_letras + 1
        palabra = palabra + letra 
print(f"la palabra '{palabra}' tiene {cantidad_letras} letras.")
