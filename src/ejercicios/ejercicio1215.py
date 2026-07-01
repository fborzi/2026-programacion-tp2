"""Este programa solicita el ingreso de una cadena de caracteres e informe
 que vocales (mayusculas y minusculas)posee la cadena,sin repetir."""


cadena = input("Ingrese una cadena de texto: ")

vocales = "aeiouAEIOU"
vocales_encontradas = set()

for caracter in cadena:
    if caracter in vocales:
        vocales_encontradas.add(caracter)

print("Las vocales que aparecen en la cadena son:", sorted(vocales_encontradas))