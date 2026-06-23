"""Escribi un programa que solicite el ingreso de un numero entero, si el numero leido es 
par, imprima la leyenda "el numero es par ". en caso contrario debera mostrar el texto El 
numero es impar"""

numero_entero = int(input("ingrese un numero entero"))

validacion = (numero_entero % 2)

if validacion == 0 :
   print("el numero es par") 
else :
   print("El numero es impar")
   