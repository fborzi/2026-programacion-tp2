a, b = 0, 1
suma = 0
for i in range(25):
    print(a)        
    suma += a       
    a, b = b, a + b 
print("La suma de los primeros 25 numeros es:", suma)