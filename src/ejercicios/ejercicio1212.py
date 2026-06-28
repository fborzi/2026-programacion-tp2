num = int(input("ingresa un número mayor que 1: "))
while num <= 1:
    num = int(input("Error el número debe ser mayor que 1.Reingresa: "))
    es_primo = True # Arranco suponiendo que si es primo
    for i in range (2, num):
        if num % i == 0: # si tiene resto cero, se divide exacto
            es_primo = False
            break # ya encontre un divisor  no hace falta seguir
        if es_primo
         print(f"{num}es primo")
     else:
        print(f"{num}no es primo"))
            