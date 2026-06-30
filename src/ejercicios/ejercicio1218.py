titulo = input()

# convertir todo a minúscula
titulo = titulo.lower()

# primera letra en mayúscula + resto igual
resultado = titulo[0].upper()

for i in range(1, len(titulo)):
    resultado += titulo[i]

print(resultado)
