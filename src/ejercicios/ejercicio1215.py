"""en este ejercicio pide ingresar una cadena e informar las vocales sin repetir"""
cadena = input("Ingrese una cadena: ")
cadena = cadena.lower()
resultado = ""
if "a" in cadena:
    resultado += "a "
if "e" in cadena:
    resultado += "e "
if "i" in cadena:
    resultado += "i "
if "o" in cadena:
    resultado += "o "
if "u" in cadena:
    resultado += "u "
print(resultado.strip())
