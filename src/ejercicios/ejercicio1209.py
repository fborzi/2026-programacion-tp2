aprobados = 0
desaprobados = 0

alumno = int(input("Ingrese número de alumno: "))

while alumno != 0:
    nota = int(input("Ingrese nota: "))

    if nota > 4:
        aprobados += 1
    else:
        desaprobados += 1

    alumno = int(input("Ingrese número de alumno: "))

print("La cantidad de aprobados es:", aprobados)
print("La cantidad de desaprobados es:", desaprobados)