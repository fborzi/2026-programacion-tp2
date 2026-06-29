""" Solicito al usuario ingresar una frase e inicializo contador palabras como string vacio
para ir acumulando las letras de cada palabra.
Recorro la frase letra por letra con un bucle for:
si encuentro un espacio imprimo la palabra acumulada y reseteo palabra a string vacio
para empezar a acumular la siguiente.
Si no encuentro un espacio acumulo la letra actual en palabra.
Al terminar el bucle imprimo la ultima palabra que no tiene espacio al final. """

frase = input("Ingrese una frase: ").strip()
contador_palabras = ""

for letra in frase:
    if letra == " ":
        print(contador_palabras)
        contador_palabras = ""
    else:
        contador_palabras = contador_palabras + letra
print(contador_palabras)
