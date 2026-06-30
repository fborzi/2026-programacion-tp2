"""Este programa solicita al usuario el ingreso de un número entero mayor
que 1 y verifica si es primo o no, analizando si posee divisores
distintos de 1 y de sí mismo. Finalmente, informa el resultado
correspondiente según las características del número ingresado."""

num = int(input("Ingrese un numero mayor que 1: "))

while num <= 1:
      num = int(input("Ingrese un número mayor que 1: "))

es_primo = True

for i in range(2, num):
    if num % i == 0:
        es_primo = False
        break
    

if es_primo:
    print(f"El numero {num} es PRIMO")
else:
    print(f"El numero {num} NO es PRIMO")
