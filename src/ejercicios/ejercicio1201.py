suma= 0
resta = 0
multiplicacion = 0
valor_absoluto1 = 0
valor_absoluto2 = 0
division =0.0
division_entera = 0
resto= 0


numero1 = int(input("ingresa el primer numero entero: "))
numero2 = int (input("ingresa el segundo numero entero: "))
# mostrar resultado



# operaciones
suma= numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
valor_absoluto1 = abs(numero1) 
valor_absoluto2 = abs(numero2)
#para división cuidamos que no divida por 0
if numero2 != 0 :
  division = numero1 / numero2
  division_entera = numero1 // numero2
  resto= numero1 % numero2
else: 
    division = "Error: no se puede dividir por 0"
    #mostrar resultados
print (suma)
print(resta)
print(multiplicacion )
print(division )
print(division_entera )
print(resto)
print(valor_absoluto1)
print(valor_absoluto2)