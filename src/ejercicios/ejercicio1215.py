""" Solicito al usuario ingresar una cadena de texto y la convierto a minusculas con .lower()
para manejar mayusculas y minusculas indistintamente.
Defino VOCALES con todas las vocales con y sin acento.
Inicializo vocales_encontradas como string vacio para acumular las vocales encontradas.
Recorro la cadena letra por letra: si la letra es una vocal y no fue encontrada antes,
la acumulo en vocales_encontradas.
Al finalizar, muestro las vocales encontradas sin repeticion. """

cadena = input("Ingrese una cadena de texto: ").lower()
VOCALES = "aáeéiíoóuú"
vocales_encontradas = ""

for letra in cadena:
    if letra in VOCALES and letra not in vocales_encontradas:
        vocales_encontradas = vocales_encontradas + letra

print(f"Las vocales que aparecen en la cadena son: {vocales_encontradas}")
