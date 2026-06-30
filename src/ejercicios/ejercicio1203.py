"""Este programa solicita el ingreso de dos números enteros y compara sus
valores para determinar si el primero es mayor, menor o igual que el
segundo, mostrando un mensaje acorde al resultado de la comparación."""

x = int(input("Ingrese un numero entero: "))
y = int(input("Ingrese un numero entero: "))

mensaje = ""

if x > y:
    mensaje = str(x) + " es mayor que " + str(y) + "."
elif x < y:
    mensaje = str(x) + " es menor que " + str(y) + "."
else:
    mensaje = str(x) + " es igual a " + str (y) + "."

print(mensaje)