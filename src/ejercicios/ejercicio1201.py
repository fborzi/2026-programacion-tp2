"""en este ejercicio se pide al usuario ingresar dos numeros enteros, luego
se trabajara sobre los mismos, se sacara la suma, resta, multiplicscion, division
con  resto y division entera. una vez realizadas las operaciones imprimiremos los resultados de cada una de las operaciones realizadas.
"""

numero1 = int(input("Ingrese primer numero entero:"))
numero2 = int(input("Ingrese segundo numero entero:"))


print("la suma de los numeros es:", numero1 + numero2)
print("la resta del primer numero con respecto al segundo es:", numero1 - numero2)
print("la multiplicacion de los numeros es:", numero1 * numero2)
if numero2 != 0:
    print("la division del primer numero y el segundo es:", numero1 / numero2)
    print("el resto de la division entre el primer numero y el segundo es:", numero1 % numero2)
    print("la division entera de entre el primer numero y el segundo es:", numero1 // numero2)
else:
    print("No se puede dividir por CERO")
    print("No es posible sacar el resto de la division por CERO")    
    print("No se hacer la division entera por CERO")
    
print("El valor absoluto del primer numero es:", abs(numero1))
print("El valor absoluto del segundo numero es:", abs(numero2))