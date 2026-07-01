texto = input("Ingrese el texto a encriptar: ")
corrimiento = int(input("Ingrese el corrimiento: "))
abecedario = "abcdefghijklmnopqrstuvwxyz"
resultado = ""
for c in texto:
    if c.lower() in abecedario:  
        
        pos = abecedario.index(c.lower())
        nueva_pos = (pos + corrimiento) % len(abecedario)
        nueva_letra = abecedario[nueva_pos]

       
        if c.isupper():
            resultado += nueva_letra.upper()
        else:
            resultado += nueva_letra
    else:
        
        resultado += c

print("Texto encriptado:", resultado)