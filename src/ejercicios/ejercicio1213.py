cantprimos = 0
 
while True:
    num= int(input("Ingrese un numero mayor a 1:"))
    if num == 0:
       break

    primo = True

    for i in range(2,num):
        if num % i == 0:
            primo = False 
            break
    
    if primo:
        cantprimos += 1
        

print("Cantidad de numeros ingresados:",cantprimos)
