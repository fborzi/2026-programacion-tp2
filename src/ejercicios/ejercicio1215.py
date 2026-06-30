"""Este programa solicita al usuario el ingreso de una cadena de caracteres
y luego recorre cada letra para identificar cuáles son vocales (a, e, i, o, u),
sin distinguir entre mayúsculas y minúsculas.
Las vocales encontradas se almacenan sin repetirse y finalmente se muestran
en pantalla separadas por un espacio.
"""

cadena = input("Ingrese una cadena: ")

vocales = "aeiou"
resultado = ""

for letra in cadena:
    letra = letra.lower()

    if letra in vocales:
        if letra not in resultado:
            resultado += letra

print("Las vocales que aparecen en la cadena son:", " ".join(resultado))
