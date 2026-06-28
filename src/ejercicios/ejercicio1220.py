texto = input ("ingresá el texto a encriptar: ")
dezplazamiento = int(input("Ingresá la cantidades de ligares a correr: "))
texto_encriptado =""
for letra in texto:
    if letra.isalpha() 
    # me fijo si es mayúscula o minúscula para no mezclar
    es_mayuscula = letra.isupper()
    # paso todo a base 0: A=0,b=1...z=25
    base = ord('A') if es_mayuscula
else ord('a')
    # Aplico la fórmula del cesar:(posición + desplazamiento)% 26
    nueva_posición = (ord(letra) - base + desplazamiento) % 26
    # vuelvo el número a letra 
    letra_encriptada = chr(base + nueva_posición)
    texto_encriptado +=
    letra_encriptada
else:texto_encriptado +=letra
   print(f"/ntexto original: {texto}")
   print(f"texto encriptado:{texto_encriptado}")
    