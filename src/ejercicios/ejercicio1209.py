aprobados = 0
desaprobados = 0

while True:
    alumno = int(input())

    if alumno == 0:
        break

    nota = int(input())

    if nota > 4:
        aprobados = aprobados + 1
    else:
        desaprobados = desaprobados + 1

print("La cantidad de aprobados es:", aprobados)
print("La cantidad de desaprobados es:", desaprobados)