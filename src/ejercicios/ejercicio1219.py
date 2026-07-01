cadena= input("ingrese una cadena:")
palabra=""

for letra in cadena :
    if letra != " " :
        palabra= palabra+letra
    else :
        print(palabra)
        palabra=""
if palabra != "" :
    print(palabra)  
    