a = 0
b = 1
suma = 0

for i in range(25):
    print(a)
    suma = suma + b
    a, b = b, a + b
    
print("suma total:",suma)    