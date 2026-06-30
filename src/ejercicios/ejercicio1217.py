resultado = ""

car = input()

while True:
    if len(car) != 1 or car == "0":
        break

    resultado += car
    car = input()

print(resultado)
