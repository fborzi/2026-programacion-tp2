"""Este programa solicita al usuario el ingreso de caracteres de longitud 1,
uno por uno, y va formando un string con todos los caracteres ingresados.
La carga de datos finaliza cuando el usuario ingresa el carácter "0"
o cuando ingresa un string cuya longitud no es 1.
Durante la ejecución, cada carácter válido se concatena a un resultado final,
que luego se muestra por pantalla."""

caracter = input("Ingrese un caracter: ")

resultado = ""

while caracter != "0" and len(caracter) == 1:
    resultado += caracter
    caracter = input("Ingrese un caracter: ")

print (resultado)

