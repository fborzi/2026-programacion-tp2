num= int(input("Ingrese un numero mayor a 1:"))

primo = True

for i in range(2,num):
 if num % i == 0:
  primo = False
 
if primo:
    print("El numero",num,"es PRIMO")
else: 
    print("El numero",num,"no es PRIMO")
