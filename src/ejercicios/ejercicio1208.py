"""
En el siguiente ejercicio solamente lo que hace es ingresar automticamente
el numero 0 y de ahi consecutivamente los siguientes numeros sumando
siempre el anterior.
"""
a = 0
b = 1
suma = 0

for i in range(25):
    print(a)
    suma += a
    c = a + b
    a = b
    b = c

while numero <= 46368:
    print(numero)
