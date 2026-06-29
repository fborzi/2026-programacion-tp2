"""
En el ejercicio 1202 pide que el usuario ingrese un numero y verifica si es menor al numero indicado. Utilizo una estructura codicional para 
indicar si es menor o mayor a 10, o en tal caso indicar si es igual. Por ultimo agrego un  mensaje que ve el usuario indicando el resultado de la
comparacion.

"""
nro= int(input("Ingrese un numero:"))
if nro > 10:
 print("El numero es mayor que 10")
else:
  if nro == 10:
   print("El numero es igual a 10")
  else:
   print("El numero es menor que 10")
