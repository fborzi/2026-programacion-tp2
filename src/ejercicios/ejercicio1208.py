"""En este ejercicio vamos a realizar la suma de los primeros 25 numeros de fibonacci"""
fibonacci = [0, 1]
for i in range(25):
    siguiente_numero = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(siguiente_numero)
    print(fibonacci[i])
