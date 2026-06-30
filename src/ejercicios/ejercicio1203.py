"""Este ejercicio es la continuacion del 1202 por lo que pediremos el ingreso de dos numeros enteros, luego compararemos 
ambos para saber si el primero numero es mayor, menor o igual al segundo numero, una vez comprobado compartiremos el resultado"""
numero1 = int(input("Ingrese primer numero entero:"))
numero2 = int(input("Ingrese segundo numero entero:"))
if numero1 > numero2:
    print(numero1, "es mayor que", numero2)
elif numero1 == numero2:
    print(numero1, "es igual a", numero2)
else:
    print(numero1, "es menor que", numero2)
