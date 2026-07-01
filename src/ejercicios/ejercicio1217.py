"""
Concatena caracteres de a uno hasta recibir algo distinto de un único carácter o "0".
"""
resultado = ""

while True:
    entrada = input("Ingrese un caracter de a uno hasta ingresar 0 para salir:")
    if len(entrada) != 1 or entrada == "0":
        break
    resultado += entrada

print(resultado)