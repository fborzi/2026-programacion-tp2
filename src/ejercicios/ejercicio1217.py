"""Ejercicio 1217 - Formar string con caracteres"""

string_completo = ""
continuar = True

while continuar:
    caracter = input("Ingresá un carácter: ")
    
    if len(caracter) != 1 or caracter == "0":
        continuar = False
    else:
        string_completo += caracter

print(string_completo)