""" Calcular e imprimir la suma de los primeros 25 numero de la sucesion de Fibonacci,
la sucesion comienza con los numeros 0 y 1, a partir de estos cada elemento es la suma de los
dos numeros anteriores en la secuencia """

primer_numero = 0
segundo_numero = 1

print(primer_numero)
print(segundo_numero)

for i in range(23) :
    suma = primer_numero + segundo_numero
    primer_numero = segundo_numero
    segundo_numero = suma
    print(suma)
    