n = int(input())

positivos = 0
negativos = 0
ceros = 0

while n != -1:
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1
    else:
        ceros += 1
    n = int(input())

print(positivos)
print(negativos)
print(ceros)
