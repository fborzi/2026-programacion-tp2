"""Este programa solicita el ingreso de un número entero y determina si el
valor ingresado es mayor que 10 o no es mayor a 10 o es igual a 10, informando el resultado correspondiente
al usuario."""

num = int(input("Ingrese un numero entero: "))

if num > 10:
    mensaje = "El numero es mayor que 10."
elif num < 10:
    mensaje = "El numero es menor que 10."
else:
    mensaje = "El numero es igual a 10."

print(mensaje)
