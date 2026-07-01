"""Este programa solicita el ingreso de string de longitud 1 uno por vez,
la repeticion terminara cuando se ingrese un string que no tenga longitud 1 o cuando el string ingresado
corresponda al caracter '0', al final mostrar el string completo que se formo con los caracteres ingresados."""


cadena = ""
while True:
    caracter = input("Ingrese un caracter (string de longitud 1) o '0' para terminar: ")
    if len(caracter) != 1 or caracter == '0':
        break
    cadena += caracter

print("String completo formado:", cadena)
