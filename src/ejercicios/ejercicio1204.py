"""solicito un numero entero y calculo el resto de dividirlo por 2 almacenandolo en validacion.
si validacion es cero el numero es par, en caso contrario es impar, e imprimo el resultado correspondiente."""

numero_entero = int(input("ingrese un numero entero"))

validacion = (numero_entero % 2)

if validacion == 0:
   print("el numero es par.") 
else :
   print("El numero es impar.")
   