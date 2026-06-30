"""inicialice los dos primeros numeros de fibonacci en 0 y 1 e imprimo ambos para obtener la salida solicitada en
el enunciado.
utilice un for de 23 vueltas porque los dos primeros ya estan impresos y la sucesion es de 25 numeros,
en cada vuelta calculo el siguiente sumando los dos anteriores, actualizo primer_numero con el valor
de segundo_numero y segundo_numero con la nueva suma, luego imprimo el resultado de cada vuelta."""

primer_numero = 0
segundo_numero = 1

print(primer_numero)
print(segundo_numero)

for i in range(23):
    suma = primer_numero + segundo_numero
    primer_numero = segundo_numero
    segundo_numero = suma
    print(suma)
