cadena=input("Ingrese una cadena de texto:")
vocales = ['a','e','i','o','u']
listaContiene=[]

for caracter in cadena :
    letra=caracter.lower()
    if letra in vocales :   
        if letra not in listaContiene:
            listaContiene.append(letra)   
print("La cadena contiene las siguientes vocales:", listaContiene)
