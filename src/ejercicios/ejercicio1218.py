texto = input().strip().lower()

if len(texto) > 0:
    resultado = texto[0].upper() + texto[1:]
else:
    resultado = ""

print(resultado)
