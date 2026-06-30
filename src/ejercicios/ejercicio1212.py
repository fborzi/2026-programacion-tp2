num = int(input())

if num > 1:
    primo = True

    for i in range(2, num):
        if num % i == 0:
            primo = False
            break

    if primo:
        print("el numero", num, "es PRIMO")
    else:
        print("el numero", num, "no es PRIMO")
else:
    print("el numero", num, "no es PRIMO")
