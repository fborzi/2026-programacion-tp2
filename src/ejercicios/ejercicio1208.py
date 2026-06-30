numero = 25
a = 0
b = 1
suma_total = 0

for i in range(numero):
    print(a)
    suma_total = suma_total + a
    a, b = b, a + b
    
print(f"la suma total es: {suma_total}")    