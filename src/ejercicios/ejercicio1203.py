"""este programa compara dos numeros enteros enteros e indica cual es mayor, menos o si son iguales"""
x = int(input("es mayor: "))
y = int(input("es menor: "))

if x > y:
    print(f"{x} es mayor que {y}.")
elif x < y:
    print(f"{x} es menor que {y}.")  
else:
    print(f"{x} es igual a {y}.")
    