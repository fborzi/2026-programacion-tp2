"""Este programa solicita el ingreso de un número entero y determina si es
par o impar verificando el resto de su división entre 2, mostrando luego
el mensaje correspondiente según el resultado obtenido."""

num = int(input("Ingrese un numero entero:"))

mensaje = ""

if num % 2 == 0:
    mensaje = "El número " + str(num) + " es PAR." 
else: 
    mensaje = "El número " + str(num) + " es IMPAR." 

print (mensaje)
