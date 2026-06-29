"""Solicito al usuario ingresar un caracter antes del loop para poder entrar en el mismo.
Inicializo acumulador_string como string vacio para ir acumulando los caracteres.
El bucle while se ejecuta mientras el caracter tenga longitud 1 y sea distinto de "0"
(entre comillas porque input() siempre devuelve un string).
Dentro del loop acumulo el caracter en acumulador_string antes de pedir el siguiente,
para evitar acumular el caracter de corte que termina el loop.
Al finalizar imprimo la cadena completa formada con todos los caracteres ingresados. """

caracter = input("ingrese un caracter: ")
acumulador_string = ""

while len(caracter) == 1 and caracter != "0":
    acumulador_string = acumulador_string + caracter
    caracter = input("ingrese un caracter: ")
    
print(acumulador_string)
