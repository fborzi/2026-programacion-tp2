"""en este ejercicio se pide al usuario ingresar dos numeros enteros, luego
se trabajara sobre los mismos, se sacara la suma, resta, multiplicscion, division
con  resto y division entera. una vez realizadas las operaciones imprimiremos los resultados de cada una de las operaciones realizadas.
"""
suma = 0
resta = 0
multiplicacion = 0
division = 0
resto = 0
division_entera = 0
numero1 = int(input("Ingrese primer numero entero:"))
numero2 = int(input("Ingrese segundo numero entero:"))
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
if numero2 != 0:
    division = numero1 / numero2
    resto = numero1 % numero2
    division_entera = numero1 // numero2
print("la suma de los numeros es:", suma)
print("la resta del primer numero con respecto al segundo es:", resta)
print("la multiplicacion de los numeros es:", multiplicacion)
print("la division del primer numero y el segundo es:", division)
print("el resto de la division entre el primer numero y el segundo es:", resto)
print("la division entera de entre el primer numero y el segundo es:", division_entera)
print("El valor absoluto del primer numero es:", abs(numero1))
print("El valor absoluto del segundo numero es:", abs(numero2))
