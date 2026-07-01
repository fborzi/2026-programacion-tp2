"""
Genera los primeros 25 términos de Fibonacci actualizando dos variables en cada vuelta.
"""
a = 0
b = 1

for _ in range(25):
    print(a)
    siguiente = a + b
    a = b
    b = siguiente
