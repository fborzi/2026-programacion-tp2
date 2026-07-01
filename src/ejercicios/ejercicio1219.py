frase = input("Ingrese una frase: ")
palabra = ""
for caracter in frase:
    if caracter != " ":   
        palabra += caracter
    else:
        print(palabra)    
        palabra = ""     
if palabra != "":
    print(palabra)
