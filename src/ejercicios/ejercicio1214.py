"""En este ejercicio pediremos el ingreso de una cadena de caracteres en el cual contaremos cantidad de 
palabras de la cadeba de caracteres y la cantidad de letras de cada palabra"""
texto = input("ingrese cadena de caracteres: ")
cadena = texto.strip()
cant_pala = 0
letr_pala = 0
pala_cade = ""
for caracter in cadena:
    if caracter != " ":
        letr_pala = letr_pala + 1
    elif letr_pala > 0:
            cant_pala = cant_pala + 1
            letr_pala = 0
print("La cantidad de palabras en la cadena es:", cant_pala + 1)
letr_pala = 0
for caracter in cadena:
    if caracter != " ":
        pala_cade = pala_cade + caracter
        letr_pala = letr_pala + 1
    elif letr_pala > 0:
            print("La palabra", '"' + pala_cade + '"', "tiene", letr_pala, "letras.")
            pala_cade = ""
            letr_pala = 0
if letr_pala > 0:
    print("La palabra", '"' + pala_cade + '"', "tiene", letr_pala, "letras.")
