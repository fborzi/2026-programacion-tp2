""" en este ejercicio pide ingresar el titulo de un libro y cuando se imprima se muestre el nombre 
con mayuscula la primera letra, no usar capitalize()"""
titulo = input("Ingrese el titulo del libro: ")
titulo = titulo.strip()
resultado = ""
for i in range(len(titulo)):
    if i == 0:
        resultado += titulo[i].upper()
    else:
        resultado += titulo[i].lower()
print(resultado)
