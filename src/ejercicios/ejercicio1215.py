texto = input("ingresá una cadena de caracteres: ")
texto = texto.lower() # Todo en minuscula para que A = a
vocales_encontradas = set() # un set no permite repetidos
vocales = "aeiou"
for letra in texto :
    if letra in vocales:
        vocales_encontradas.add(letra) # lo agrega solo si no esta 
        vocales_ordenadas = sorted(vocales_encontradas)
        if vocales_ordenadas:
            print(f"las vocales que aparecen sin repetir son :{".join(vocales_ordenadas)"}")
        else:
            print("No se encontraron vocales en la cadena")
