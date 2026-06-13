"""Este programa solicita el ingreso de dos numeros enteros y luego informa 
si el primero es o no mayor que el segundo, usando 'x' para un numero y 'y'
para el otro"""

num_1=int(input("Ingrese el primer numero entero: "))
num_2=int(input("Ingrese el segundo numero entero: "))

if num_1 > num_2:
    print(num_1,"es mayor que",num_2)
elif num_1 < num_2:
    print(num_1,"es menor que",num_2)
else:
    print(num_1,"es igual a",num_2)