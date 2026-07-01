"""Este programa analiza una cadena de texto e informa sus palabras y caracteres."""
cadena = input("ingrese una cadena de texto: ")

contador_palabra = 0
contador_letra = 0
palabra = ""

cadena = cadena + ""

for caracter in cadena:
    if caracter != " ":
        contador_letra = contador_letra + 1
        palabra = palabra + caracter
    else:
        if contador_letra > 0:
           contador_palabra = contador_palabra + 1
           print(f"la palabra '{palabra}' tiene {contador_letra} letra.")
           contador_letra = 0
           palabra = ""
        
print(f"la cantidad de palabra en la cadena es: {contador_palabra}")