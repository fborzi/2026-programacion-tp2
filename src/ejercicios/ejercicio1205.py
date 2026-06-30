"""Este programa solicita el ingreso del día de la semana y la cantidad de
artículos comprados por un cliente. Luego verifica si el día ingresado
es lunes y si se compraron más de tres artículos para determinar si el
cliente accede al descuento, mostrando el mensaje correspondiente en
caso de cumplir ambas condiciones."""

dia = input("Ingrese el día de la semana: ")
articulos = int(input("Ingrese la cantidad de artículos: "))

mensaje = ""

if dia == "lunes" and articulos > 3:
    mensaje = "accede al descuento"

print(mensaje)