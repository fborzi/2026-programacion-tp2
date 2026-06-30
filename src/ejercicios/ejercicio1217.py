"escribi un programa que lee caracteres del usuario hasta que se ingrese '0' y forme un string con ellos."
resultado = ""
char = input("")

while char != "0" and len(char) == 1:
    resultado += char
    char = input("")

print("El string formado es: " + resultado)
