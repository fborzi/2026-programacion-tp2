texto = input("Ingresá una cadena de texto:")
# .split()separa por espacios y saca los espacios de mas
palabras = texto.split()
cantidad_palabras = len(palabras)
print(f"/nLa cadena tiene {cantidad_palabras} palabra ")
print("/nCantidad de caracteres por palabra:")
for i , palabra in enumerate(palabras,start =1):
    cantidad_letras = len(palabra)
    print(f"palabra {i} " {palabra}":{cantidad_letras}caracteres")
    