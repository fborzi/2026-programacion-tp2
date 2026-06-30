aprobados = 0
desaprobados = 0

alumno = int(input())
nota = int(input())

while alumno != 0:
    if nota > 4:
        aprobados += 1
    else:
        desaprobados += 1

    alumno = int(input())
    if alumno != 0:
        nota = int(input())

print("la cantidad de aprobados es:", aprobados)
print("la cantidad de desaprobados es:", desaprobados)
