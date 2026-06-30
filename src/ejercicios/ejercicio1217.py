"escribi un programa que lee caracteres del usuario hasta que se ingrese '0' y forme un string con ellos."
resultado = ""
char = input("Ingrese un caracter (o '0' para terminar): ")

while char != "0" and len(char) == 1:
    resultado += char
    char = input("")

print(f"El string formado es: {resultado}")
