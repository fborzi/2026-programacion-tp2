numero = int(input("ingrese un numero mayor que 1: "))

es_primo = True

for divisor in range(2, numero):
    if numero % divisor == 0:
        es_primo
        
if es_primo == True:
    print("el numero", numero, "es PRIMO,")
else:
    print("elnumero", numero, "no es PRIMO,")
        