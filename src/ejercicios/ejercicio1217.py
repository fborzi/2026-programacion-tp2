resultado = ""

car = input()

while len(car) == 1 and car != "0":
    resultado += car
    car = input()

print(resultado)
