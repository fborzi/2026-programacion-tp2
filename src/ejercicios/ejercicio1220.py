"""Escribí un programa que permita encriptar un texto dado por el usuario y lo imprima. Para ello se utilizará un método muy antiguo, llamado "la cifra del César", que consiste en correr cada letra una determinada cantidad de lugares. Por ejemplo, si corremos las letras 2 lugares, la palabra "hola" se transforma en "jqnc". Si el abecedario termina antes de poder correr la cantidad de lugares necesarios, se vuelve a comenzar desde la letra "a". Así, la palabra "extra" corrida 3 lugares se convierte en "hawud". La cantidad de lugares que se correrán las letras será dada por el usuario.

Pista: para sortear el obstáculo de que se "termine" el abecedario al intentar correr una letra, podemos usar el siguiente cálculo matemático: (indice de la letra a correr+corrimiento)%27 (si utilizamos el alfabeto español de 27 letras).

Si alguno de los caracteres en la frase no es una letra, se la debe dejar como está, sin encriptar"""

texto = input("Ingrese un texto: ")
corrimiento = int(input("Ingrese la cantidad de lugares a correr: "))

encriptado = ""
for caracter in texto:
    if caracter.isalpha():
   
        caracter = caracter.lower()
       
        nuevo_indice = (ord(caracter) - ord('a') + corrimiento) % 27
        
        nuevo_caracter = chr(nuevo_indice + ord('a'))
        encriptado += nuevo_caracter
    else:
        encriptado += caracter

print("Texto encriptado:", encriptado)
