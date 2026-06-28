"""
En el ejercicio 1219 se pide que se ingrese una frase.
Luego el programa va ejecutando palabra por palabra y a medida
que encuentra un espacio pasa a la siguiente palabra y asi
sucesivamente hasta no encontrar mas palabras y finaliza
imprimiendo en pantalla una palabra debajo de otra. 
"""
frase = input("Ingrese una frase: ")

palabra = ""

for letra in frase:
    if letra != " ":
        palabra += letra
    else:
        print(palabra)
        palabra = ""
print(palabra)
