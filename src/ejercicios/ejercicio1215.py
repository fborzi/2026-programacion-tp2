cadena = input("ingrese  una cadena caracteres: ")

cadena = cadena.lower()
encontro_a = False
encontro_e = False
encontro_i = False
encontro_o = False
encontro_u = False

vocales_encontradas =""

for caracter in cadena:
    if caracter == "a" and encontro_a == False:
        vocales_encontradas = vocales_encontradas + "a"
        encontro_a = True
    elif caracter == "e" and encontro_e == False:
        vocales_encontradas = vocales_encontradas + "e"
        encontro_e = True
    elif caracter == "i" and encontro_i == False:
        vocales_encontradas = vocales_encontradas + "i"
        encontro_i = True
    elif caracter == "o" and encontro_o == False:
        vocales_encontradas = vocales_encontradas + "o"
        encontro_o = True
    elif caracter == "u" and encontro_u == False:
        vocales_encontradas = vocales_encontradas + "u"
        encontro_u = True
        
print("las vocales que aparecen en la cadena son:", vocales_encontradas)