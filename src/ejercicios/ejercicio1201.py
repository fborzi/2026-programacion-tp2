a = int(input())
b = int(input())

print(a + b)
print(a - b)
print(a * b)

if b != 0:
    print(a // b)
    print(a % b)
else:
    print("No se puede dividir por cero")
    print("No se puede calcular resto")

print(abs(a))
print(abs(b))
