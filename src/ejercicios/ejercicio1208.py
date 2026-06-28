n = 25
a,b = 0,1 # los dos primeros numeros de fibonacci
suma_total = 0
print("Los primeros 25 números de Fibonacci:")
for i in range (n):
    print(a,end="") # para que salgan en la misma linea 
    suma_total += a # voy sumando cada termino
    a,b = b, a + b # Avanzo en la secuencia : el nuevo a es el b viejo
    print(f"/n/nsuma de los primeros 25 números :{suma_total}")